from collections import namedtuple, defaultdict
from itertools import repeat
from HeapHelper import MinHeap

inf = float('inf')
Edge = namedtuple('Edge', ['tail', 'head', 'weight'])

class Graph:
    
    def __init__(self):
        self._adjacency_list = defaultdict(list)
        self._edges = set()
    
    def read_input(self, filename):
        with open(filename, 'r') as f:
            line = f.readline()
            while line:
                tail = int(line.split()[0])
                edges = line.split()[1:]
                for e in edges:
                    head, weight = list(map(int, e.split(','))) 
                    edge = Edge(tail, head, weight)
                    self._adjacency_list[tail].append(edge)
                    self._edges.add(edge)
                    if head not in self._adjacency_list:
                        self._adjacency_list[head] = []
                line = f.readline()
    
    def get_neighbours(self, vertex):
        return self._adjacency_list[vertex]

    @property
    def vertices(self):
        return set(self._adjacency_list.keys())

    @property
    def edges(self):
        return self._edges

def dijkstra(source_vertex, graph):
    assert source_vertex in graph.vertices
    print('Starting Dijkstra shortest path...')
    shortest_dist = {vertex: inf for vertex in graph.vertices}
    shortest_dist[source_vertex] = 0
    dijkstra_score = defaultdict(set)
    dijkstra_score[inf] = graph.vertices
    dijkstra_score[inf].remove(source_vertex)
    dijkstra_score[0].add(source_vertex)
    to_heapify = [item for sublist in [list(repeat(key, len(value))) for key, value in dijkstra_score.items()] for item in sublist]
    unprocessed = MinHeap()
    unprocessed.build_heap(to_heapify)
    print('Starting the main loop...')
    while unprocessed.size > 0:
        min_dijkstra_score = unprocessed.extract_min()
        chosen_vertex = dijkstra_score[min_dijkstra_score].pop()
        shortest_dist[chosen_vertex] = min_dijkstra_score
        for edge in graph.get_neighbours(chosen_vertex):
            vertex_to_update = edge.head
            score_to_remove = shortest_dist[vertex_to_update]
            new_score = min(score_to_remove, shortest_dist[chosen_vertex]+edge.weight)
            shortest_dist[vertex_to_update] = new_score
            if score_to_remove is not new_score:
                unprocessed.delete(score_to_remove)
                unprocessed.insert(new_score)
                dijkstra_score[new_score].add(vertex_to_update)
                dijkstra_score[score_to_remove].remove(vertex_to_update)
    return shortest_dist

if __name__ == '__main__':

    graph = Graph()
    print('Reading input...')
    graph.read_input('dijkstraData.txt')

    source = 1
    shortest_path = dijkstra(source, graph)
    
    test = [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]
    for num in test:
        print('shortest path to vertex {}:'.format(num), shortest_path[num])

    """ 
    Correct answers
    shortest path to vertex 7: 2599
    shortest path to vertex 37: 2610
    shortest path to vertex 59: 2947
    shortest path to vertex 82: 2052
    shortest path to vertex 99: 2367
    shortest path to vertex 115: 2399
    shortest path to vertex 133: 2029
    shortest path to vertex 165: 2442
    shortest path to vertex 188: 2505
    shortest path to vertex 197: 3068 
    """


