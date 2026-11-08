class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.dict = {}
        for start, end in self.edges:
            if start in self.dict:
                self.dict[start].append(end)
            else:
                self.dict[start] = [end]

    def get_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.dict:
            return []
        paths = []
        for node in self.dict[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.dict:
            return None
        paths = []
        shortest_path = None
        for node in self.dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto"),
]

grape_routes = Graph(routes)


# This is better DS than ABove Lets convert into dict
# d={
#     "Mumbai":["Paris","Dubai"],
#     "Paris":["Dubai","New York"]
# }

start = "Mumbai"
end = "New York"


print("All Paths:")
print(grape_routes.get_path(start, end))

print("shortest Path:")
print(grape_routes.get_shortest_path(start, end))
