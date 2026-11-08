import math
class Node:
    def __init__(self,order):
        self.order=order
        self.values=[]
        self.keys=[]
        self.nextKey=None
        self.parent=None
        self.check_leaf=False
        
    def insert_at_leaf(self,value,key):
        if(self.values):
            temp1=self.values
            for i in range(len(temp1)):
                if(value == temp1[i]):
                    self.keys[i].append(key)
                    break
                elif value < temp1[i]:
                    self.values.insert(i,value)
                    self.keys.insert(i,[key])
                    break
                elif i+1 == len(temp1):
                    self.values.append(value)
                    self.keys.append([key])
                    break
        else:
            self.values=[value]
            self.keys=[[key]]

class BplusTree:
    def __init__(self,order):
        self.root=Node(order)
        self.root.check_leaf=True

    def search(self,value):
        current_node=self.root
        while current_node.check_leaf == False:
            temp=current_node.values
            for i in range(len(temp)):
                if value == temp[i]:
                    current_node=current_node.keys[i+1]
                    break
                elif value < temp[i]:
                    current_node=current_node.keys[i]
                    break
                elif i+1 == len(current_node.values):
                    current_node=current_node.keys[i+1]
                    break
        return current_node

    
    def insert(self,value,key):
        value=str(value)
        leaf_node=self.search(value)
        leaf_node.insert_at_leaf(value,key)

        if len(leaf_node.values) == leaf_node.order:  #overflow at leaf
            node1=Node(leaf_node.order)
            node1.check_leaf=True
            node1.parent=leaf_node.parent

            mid=int(math.ceil(leaf_node.order/2))-1

            node1.values=leaf_node.values[mid+1:]
            node1.keys=leaf_node.keys[mid+1:]
            node1.nextKey=leaf_node.nextKey

            leaf_node.values=leaf_node.values[:mid+1]
            leaf_node.keys=leaf_node.keys[:mid+1]
            leaf_node.nextKey=node1

            self.insert_at_parent(leaf_node,node1.values[0],node1)
    
    def insert_at_parent(self,node,value,newnode):
        if self.root == node:
            rootNode=Node(node.order)
            rootNode.values=[value]
            rootNode.keys=[node,newnode]

            self.root=rootNode
            node.parent=rootNode
            newnode.parent=rootNode
            return
        parentNode=node.parent
        temp3=parentNode.keys
        for i in range(len(temp3)):
            if temp3[i] == node:
                parentNode.values.insert(i,value)
                parentNode.keys.insert(i+1,newnode)     
                if(len(parentNode.keys)>parentNode.order): #overflow at parent Node 
                    newNode=Node(parentNode.order)
                    newNode.parent=parentNode.parent
                    mid=int(math.ceil(parentNode.order/2))-1

                    newNode.values=parentNode.values[mid+1:]
                    newNode.keys=parentNode.keys[mid+1:]
                    val=parentNode.values[mid]


                    parentNode.values = parentNode.values[:mid]

                    parentNode.keys=parentNode.keys[:mid+1]

                    for j in parentNode.keys:
                        j.parent=parentNode
                    for j in newNode.keys:
                        j.parent=newNode
                    
                    self.insert_at_parent(parentNode,val,newNode)
                break
    

    def find(self,key,value):
        value=str(value)
        leaf_node=self.search(value)
        values=leaf_node.values
        for i in range(len(values)):
            if value == values[i]:
                if key in leaf_node.keys[i]:
                    return True
        return False
    
    def printTree(self):
        from collections import deque
        queue=deque([(self.root,0)])
        last_level=-1

        while queue:
            node,level=queue.popleft()

            if level != last_level:
                if last_level != -1:
                    print()
                last_level=level
            
            print(f"[{','.join(node.values)}]",end=" ")

            if not node.check_leaf:
                queue.extend((child,level+1) for child in node.keys)


order=int(input('enter order of tree:'))
btrue=BplusTree(order)
while(True):
    print('1.insert\t2.search\t3.display\t4.Exit\n')
    ch=int(input('enter choice:'))
    if ch==1:
        key=input('enter key:')
        val=input('enter value:')
        btrue.insert(val,key)
        print(f"inserted:{(key,val)}")
    elif ch==2:
        key=input('enter key:')
        val=input('enter value:')
        res=btrue.find(key,val)
        if res:
            print('Found')
        else:
            print('Not found')
    elif ch==3:
        btrue.printTree()
    elif ch==4:
        print('Thank You!')
        break
    else:
        print('Invalid input')






