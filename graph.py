class AdjacencyList(object):

    def __init__(self):
        self.List = {}

    def _add_edge(self, from_vertex, to_vertex):
        # check if vertex is already present
        if from_vertex in self.List.keys():
            self.List[from_vertex].append(to_vertex)
        else:
            self.List[from_vertex] = [to_vertex]

    def _print_list(self):
        for i in self.List:
            print(i, '->', ' -> '.join([str(j) for j in self.List[i]]))


def main():
    print("=== Graph - An abstract data type that is meant to implement the undirected graph and directed graph concepts consisting of a finite set of vertices or nodes or points")

    al = AdjacencyList()
    al._add_edge(0, 1)
    al._add_edge(0, 4)
    al._add_edge(4, 1)
    al._add_edge(4, 3)
    al._add_edge(1, 0)
    al._add_edge(1, 4)
    al._add_edge(1, 3)
    al._add_edge(1, 2)
    al._add_edge(2, 3)
    al._add_edge(3, 4)

    al._print_list()


if __name__=='__main__':
	main()