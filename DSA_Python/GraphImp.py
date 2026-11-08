class Graph:
    def __init__(self):
        self.graph={}
    def add_node(self,node):
        self.graph[node]=list()
    def add_edge(self,n1,n2):
        if n1 not in self.graph:
            self.add_node(n1)
        if n2 not in self.graph:
            self.add_node(n2)
        self.graph[n1].append(n2)
        self.graph[n2].append(n1)
    def DFS(self,start_node):
        visited=set()
        stack=[start_node]

        while stack:
            ele=stack.pop()
            if ele not in visited:
                visited.add(ele)
                print(ele,end=" ")
                for neigbours in self.graph[ele]:
                    stack.append(neigbours)

    def BFS(self,start_node):
        visited=set()
        queue=[start_node]

        while queue:
            ele=queue.pop(0)
            if ele not in visited:
                visited.add(ele)
                print(ele,end=" ")
                for neigbours in self.graph[ele]:
                    queue.append(neigbours)



    def display(self):
        for k,v in self.graph.items():
            print(f"{k}:{v}")

g=Graph()
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)

g.add_edge(2,5)
g.add_edge(3,5)
g.add_edge(4,5)


g.display()

g.DFS(1)
print()
g.BFS(1)
