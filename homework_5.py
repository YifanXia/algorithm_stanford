from collections import namedtuple, defaultdict

inf = float('inf')
Edge = namedtuple('Edge', ['head', 'weight'])

class Graph:
    
    def __init__(self):
        self._adjacency_list = defaultdict(list)
    
    def read_input(self, filename):
        with open(filename, 'r') as f:
            line = f.readline()
            while line:
                tail = int(line.split()[0])
                edges = line.split()[1:]
                for e in edges:
                    head, weight = list(map(int, e.split(','))) 
                    edge = Edge(head, weight)
                    self._adjacency_list[tail].append(edge)
                line = f.readline()
    
    def get_neighbours(self, vertex):
        return self._adjacency_list[vertex]

if __name__ == '__main__':

    graph = Graph()
    graph.read_input('dijkstraTest.txt')
    print(graph.get_neighbours(2))


