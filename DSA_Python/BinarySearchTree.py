class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
            return
        self.insert_value(self.root,data)
    def insert_value(self,root,data):
        if root.data>data:
            if root.left:
                self.insert_value(root.left,data)
            else:
                root.left=Node(data)
        elif root.data<data:
            if root.right:
                self.insert_value(root.right,data)
            else:
                root.right=Node(data)

    def delete(self, root, key):
        if root is None:
            return None

        # Traverse the tree
        if root.data > key:
            root.left = self.delete(root.left, key)
        elif root.data < key:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: get the in-order successor (smallest in the right subtree)
            succ=self.min_value(root.right)
            root.data=succ.data
            root.right=self.delete(root.right,succ.data)
        return root


    def min_value(self,node):
        cur=node
        while cur.left:
            cur=cur.left
        return cur


    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            print(root.data,end="-->")
            self.inOrder(root.right)
    
b=BST()
myarr=[3,1,7,12,100,23,50]

for x in myarr:
    b.insert(x)

b.inOrder(b.root)

b.root=b.delete(b.root,1)
print()
b.inOrder(b.root)

            

