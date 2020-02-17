import heapq
from collections import defaultdict
from itertools import count
from typing import List, Tuple, Dict

## Important knowledge: heapq elements can be list of tuples, the first element of each tuple is taken as key
inf = float('inf')

class Graph:

    def __init__(self):
        self._adjacency_list = defaultdict(set)
    
    def read_input(self, filename: str):
        with open(filename, 'r') as f:
            metadata = f.readline()
            ##breakpoint()
            self._num_vertices = int(metadata.split()[0])
            self._num_edges = int(metadata.split()[1])
            line = f.readline()
            while line:
                vertex1, vertex2, weight = [int(v) for v in line.split()]
                self._adjacency_list[vertex1].add((vertex2, weight))
                self._adjacency_list[vertex2].add((vertex1, weight))
                line = f.readline()
    
    @property
    def get_vertices(self):
        return set(self._adjacency_list.keys())
    
    def get_neighbours(self, vertice):
        return self._adjacency_list[vertice]

def get_index_heap(heap: List[Tuple[int, int, int]]) -> Dict[int, int]:
    """Tracks vertices' indices in a heap
    
    Arguments:
        heap {List[Tuple[int, int, int]]} -- [description]
    
    Returns:
        Dict[int, int] -- [description]
    """
    index_heap = {}
    for idx, value in enumerate(heap):
        index_heap[value[2]] = idx
    return index_heap


def prim_mst(graph: Graph) -> int:
    total = 0
    mst_vertices = set()
    unvisited = graph.get_vertices
    vertex_key = {}
    for v in unvisited:
        vertex_key[v] = inf
    v_start = unvisited.pop()
    mst_vertices.add(v_start)
    vertex_key[v_start] = 0
    tie_breaker = count().__next__
    cut_heap = [(inf, tie_breaker(), v) for v in unvisited]
    index_heap = get_index_heap(cut_heap)

    for vertex, weight in graph.get_neighbours(v_start):
        vertex_key[vertex] = weight
        cut_heap.pop(index_heap[vertex])
        cut_heap.append((weight, tie_breaker(), vertex))
        heapq.heapify(cut_heap)
        index_heap = get_index_heap(cut_heap)
    #breakpoint()

        
    while unvisited:
        min_weight, _, min_vertex = heapq.heappop(cut_heap)
        index_heap = get_index_heap(cut_heap)
        total += min_weight
        mst_vertices.add(min_vertex)
        unvisited.remove(min_vertex)
        for vertex, weight in graph.get_neighbours(min_vertex):
            if vertex not in mst_vertices:
                if vertex_key[vertex] > weight:
                    cut_heap.pop(index_heap[vertex])
                    cut_heap.append((weight, tie_breaker(), vertex))
                    heapq.heapify(cut_heap)
                    index_heap = get_index_heap(cut_heap)
                    vertex_key[vertex] = weight
    
    return total

if __name__ == '__main__':

    graph = Graph()
    print('Reading input...')
    graph.read_input('Part2/test_files/mst_tests/test_mst_5.txt')

    total = prim_mst(graph)
    print(total)




    
