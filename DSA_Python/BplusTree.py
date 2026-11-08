import math

class Node:
    def __init__(self, order):
        self.order = order
        self.values = []
        self.keys = []
        self.nextKey = None
        self.parent = None
        self.check_leaf = False

    def insert_at_leaf(self, leaf, value, key):
        if self.values:
            for i in range(len(self.values)):
                if value == self.values[i]:
                    self.keys[i].append(key)
                    break
                elif value < self.values[i]:
                    self.values = self.values[:i] + [value] + self.values[i:]
                    self.keys = self.keys[:i] + [[key]] + self.keys[i:]
                    break
                elif i + 1 == len(self.values):
                    self.values.append(value)
                    self.keys.append([key])
                    break
        else:
            self.values = [value]
            self.keys = [[key]]


class BplusTree:
    def __init__(self, order):
        self.root = Node(order)
        self.root.check_leaf = True

    def search(self, value):
        current = self.root
        while not current.check_leaf:
            for i in range(len(current.values)):
                if value == current.values[i]:
                    current = current.keys[i + 1]
                    break
                elif value < current.values[i]:
                    current = current.keys[i]
                    break
                elif i + 1 == len(current.values):
                    current = current.keys[i + 1]
                    break
        return current

    def insert(self, key, value):
        value = str(value)
        leaf = self.search(value)
        leaf.insert_at_leaf(leaf, value, key)

        if len(leaf.values) == leaf.order:
            new_leaf = Node(leaf.order)
            new_leaf.check_leaf = True
            mid = (leaf.order + 1) // 2

            new_leaf.values = leaf.values[mid:]
            new_leaf.keys = leaf.keys[mid:]
            new_leaf.parent = leaf.parent
            new_leaf.nextKey = leaf.nextKey

            leaf.values = leaf.values[:mid]
            leaf.keys = leaf.keys[:mid]
            leaf.nextKey = new_leaf

            self.insert_at_parent(leaf, new_leaf.values[0], new_leaf)

    def insert_at_parent(self, node, value, new_node):
        if node == self.root:
            new_root = Node(node.order)
            new_root.values = [value]
            new_root.keys = [node, new_node]
            node.parent = new_root
            new_node.parent = new_root
            self.root = new_root
            return

        parent = node.parent
        for i in range(len(parent.keys)):
            if node == parent.keys[i]:
                parent.values = parent.values[:i] + [value] + parent.values[i:]
                parent.keys = parent.keys[:i + 1] + [new_node] + parent.keys[i + 1:]
                break

        if len(parent.keys) > parent.order:
            new_parent = Node(parent.order)
            mid = (parent.order + 1) // 2
            promote = parent.values[mid - 1]

            new_parent.values = parent.values[mid:]
            new_parent.keys = parent.keys[mid:]
            new_parent.parent = parent.parent

            parent.values = parent.values[:mid - 1]
            parent.keys = parent.keys[:mid]

            for child in parent.keys:
                child.parent = parent
            for child in new_parent.keys:
                child.parent = new_parent

            self.insert_at_parent(parent, promote, new_parent)

    def printTree(self):
        queue = [(self.root, 0)]
        current_level = 0
        print("\n----- B+ Tree Structure -----")
        while queue:
            node, level = queue.pop(0)
            if level != current_level:
                print()
                current_level = level

            print(f"[{', '.join(node.values)}]", end="  ")

            if not node.check_leaf:
                for child in node.keys:
                    queue.append((child, level + 1))
        print("\n-----------------------------\n")

    def find(self, key, value):
        value = str(value)
        leaf = self.search(value)
        for i in range(len(leaf.values)):
            if leaf.values[i] == value:
                if key in leaf.keys[i]:
                    return True
        return False


# ---------------- Main Menu ----------------
def main():
    order = int(input("Enter the order of B+ Tree: "))
    bptree = BplusTree(order)

    while True:
        print("\n--- Menu ---")
        print("1. Insert")
        print("2. Display Tree")
        print("3. Search")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            k = input("Enter key to insert: ")
            v = input("Enter value to insert: ")
            bptree.insert(k, v)
            print(f"Inserted ({k}, {v})")
        elif choice == '2':
            bptree.printTree()
        elif choice == '3':
            k = input("Enter key to search: ")
            v = input("Enter value to search: ")
            if bptree.find(k, v):
                print("Found!")
            else:
                print("Not Found.")
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

# ---------------- Run Program ----------------
if __name__ == "__main__":
    main()
