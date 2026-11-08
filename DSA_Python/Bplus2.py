import math

class BPNode:
    def __init__(self, is_leaf=True):
        self.data = []
        self.children = []
        self.is_leaf = is_leaf
        self.next = None

class BPTree:
    def __init__(self, order=5):
        self.order = order
        self.root = BPNode()

    def insert(self, data):
        root = self.root
        new_key, new_child = self._insert_internal(root, data)
        if new_key is not None:
            new_root = BPNode(is_leaf=False)
            new_root.data = [new_key]
            new_root.children = [root, new_child]
            self.root = new_root

    def _insert_internal(self, node, data):
        if node.is_leaf:
            index = 0
            while index < len(node.data) and data > node.data[index]:
                index += 1
            node.data.insert(index, data)
            if len(node.data) >= self.order:
                return self._split_leaf(node)
            return None, None
        else:
            index = 0
            while index < len(node.data) and data > node.data[index]:
                index += 1
            new_key, new_child = self._insert_internal(node.children[index], data)
            if new_key is not None:
                node.data.insert(index, new_key)
                node.children.insert(index + 1, new_child)
                if len(node.data) >= self.order:
                    return self._split_internal(node)
            return None, None

    def _split_leaf(self, node):
        mid = self.order // 2
        right = BPNode(is_leaf=True)
        right.data = node.data[mid:]
        node.data = node.data[:mid]
        right.next = node.next
        node.next = right
        return right.data[0], right

    def _split_internal(self, node):
        mid = self.order // 2
        right = BPNode(is_leaf=False)
        right.data = node.data[mid+1:]
        right.children = node.children[mid+1:]
        new_key = node.data[mid]
        node.data = node.data[:mid]
        node.children = node.children[:mid+1]
        return new_key, right

    def search(self, data):
        node = self.root
        while node:
            if node.is_leaf:
                if data in node.data:
                    print(f"{data} is present in the B+ Tree.")
                    return True
                else:
                    print(f"{data} is not present in the B+ Tree.")
                    return False
            else:
                            i = 0
                            while i < len(node.data) and data >= node.data[i]:
                                i += 1
                            node = node.children[i]

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        indent = "    " * level
        print(indent + "Data:", node.data, "| Leaf:", node.is_leaf)
        if not node.is_leaf:
            for child in node.children:
                self.display(child, level + 1)

# Example usage
if __name__ == "__main__":
    bpt = BPTree(order=5)
    while True:
        print("\n1 - INSERT\n2 - SEARCH\n3 - DISPLAY\n4 - EXIT")
        opt = int(input("Enter option: "))
        if opt == 1:
            val = int(input("Enter value to insert: "))
            bpt.insert(val)
            print("Inserted.")
        elif opt == 2:
            val = int(input("Enter value to search: "))
            bpt.search(val)
        elif opt == 3:
            bpt.display()
        elif opt == 4:
            print("Exited.")
            break
        else:
            print("Invalid option!")