class Node:
    name = ""

    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_paths(self, current_path):

        current_path += "-"+self.name

        if self.name == "end":
            return [current_path]

        paths = []
        for c in self.children:
            if c.is_start():
                continue

            if c.is_lower() and c.name in current_path:
                continue

            child_paths = c.get_paths(current_path)

            if len(child_paths) == 0:
                continue

            for cp in child_paths:
                paths.append(cp)

        return paths

    def is_start(self):
        return self.name == "start"

    def is_end(self):
        return self.name == "end"

    def is_lower(self):
        return self.name.lower() == self.name

    def print(self):
        print(self.name)
        children = ""
        for n in self.children:
            children += " " + n.name
        print("Children: ", children)

def part1():
    f = open("./Puzzel_files/puzzel_12.txt")
    nodes = {}
    input = f.readline().strip()

    while input != "":
        names = input.split("-")

        print("names: ", names)

        node1 = nodes[names[0]] if names[0] in nodes else Node(names[0])
        node2 = nodes[names[1]] if names[1] in nodes else Node(names[1])

        nodes[names[0]] = node1
        nodes[names[1]] = node2

        node1.add_child(node2)
        node2.add_child(node1)
        input = f.readline().strip()

    for n in nodes:
        nodes[n].print()

    s = nodes["start"]

    paths = s.get_paths("")

    print(paths)
    print("Part1: ", len(paths))

part1()