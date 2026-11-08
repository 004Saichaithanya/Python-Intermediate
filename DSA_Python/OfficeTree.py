from Tree import TreeNode

class OfficeTree(TreeNode):
    def print_tree(self,text):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data)
        if self.childern:
            for child in self.childern:
                child.print_tree(text="")



def build_office_tree():
    nilupul=OfficeTree("Nilupul")
    chinmay=OfficeTree("chinmay")

    vishwa=OfficeTree("Vishwa")
    vishwa.addchild(OfficeTree("Dhaval"))
    vishwa.addchild(OfficeTree("Abhijit"))
    chinmay.addchild(vishwa)
    chinmay.addchild(OfficeTree("Aamir"))

    gels=OfficeTree("Gels")
    gels.addchild(OfficeTree("Peter"))
    gels.addchild(OfficeTree("Waqas"))

    nilupul.addchild(chinmay)
    nilupul.addchild(gels)
    return nilupul

nilupul=build_office_tree()
nilupul.print_tree("name")


