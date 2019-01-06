class Graph:

    def __init__(self):
        self.adjacency_list = {}
        self.reverse_list = {}

    def read_input_file(self, file_name):
        with open(file_name, 'r') as f:
            for edge in f:
                end_points = list(map(int, edge.split()))
                assert(len(end_points) == 2)
                start = end_points[0]
                fin = end_points[1]
                #print(start)
                
                try:
                    self.adjacency_list[start] = self.adjacency_list[start] + [fin]
                except KeyError:
                    self.adjacency_list[start] = [fin]
                
                try:
                    self.reverse_list[fin] = self.reverse_list[fin] + [start]
                except KeyError:
                    self.reverse_list[fin] = [start]
    
    def get_nodes(self):
        return self.adjacency_list.keys()

    def get_neighbours(self, v):
        if v in self.get_nodes():
            return self.adjacency_list[v]
        else:
            return None


def DFS_visit(graph, vertex, parents, finished):
    for v in graph.get_neighbours(vertex):
        if v not in parents:
            parents[v] = vertex
            DFS_visit(graph, v, parents, finished)
    finished.append(vertex)

def DFS(graph):
    parents = {}
    finished = []
    for v in graph.get_nodes():
        if v not in parents:
            parents[v] = None
            DFS_visit(graph, v, parents, finished)
    return parents, finished
                

if __name__ == '__main__':

    input_file = "SCC.txt"
    graph = Graph()
    graph.read_input_file(input_file)
    parents, finished = DFS(graph)
    print(finished)