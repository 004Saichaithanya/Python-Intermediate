class TreeNode:
    def __init__(self, data):
        self.data = data
        self.childern = []
        self.parent = None

    def addchild(self, child):
        child.parent = self
        self.childern.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.childern:
            for child in self.childern:
                child.print_tree()
    

def bulid_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptops")
    laptop.addchild(TreeNode("ThinkPad"))
    laptop.addchild(TreeNode("Dell"))
    laptop.addchild(TreeNode("Mac"))

    cellphone = TreeNode("Cell Phone")
    cellphone.addchild(TreeNode("Samsung"))
    cellphone.addchild(TreeNode("MotoRola"))
    cellphone.addchild(TreeNode("OnePlus"))

    tv = TreeNode("TV")
    tv.addchild(TreeNode("Mi tv"))
    tv.addchild(TreeNode("Panasonic"))
    tv.addchild(TreeNode("LG"))

    root.addchild(laptop)
    root.addchild(cellphone)
    root.addchild(tv)
    return root


root = bulid_product_tree()
root.print_tree()
# print(root.get_level())





