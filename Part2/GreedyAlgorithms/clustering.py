from typing import List, Tuple
from union_find import DisjointSet, Graph, Node

class ClusterFinder:
    
    def __init__(self, graph: Graph):
        self.graph = graph
        self.disjoint_set = DisjointSet(graph)
        self.cluster_number = len(self.disjoint_set.nodes)
    
    def run_union_find(self, edge: List[Tuple[int, Tuple[Node, Node]]]):
        node1, node2 = edge[1]
        set1 = DisjointSet.find(node1)
        set2 = DisjointSet.find(node2)
        if set1 == set2:
            pass
        else:
            self.cluster_number -= 1
            self.set_size = set1.set_size + set2.set_size
            DisjointSet.union(set1, set2)
    
    def find_clusters(self, num_clusters: int) -> List[Tuple[int, Tuple[Node, Node]]]:
        edges = sorted(self.graph._adjacency_list, key=lambda e: e[0])
        while self.cluster_number > num_clusters:
            edge = edges.pop(0)
            self.run_union_find(edge)
        return edges
    
    def find_max_spacing(self, num_clusters: int) -> int:
        edges = sorted(self.find_clusters(num_clusters), key=lambda e: e[0])
        for edge in edges:
            node1, node2 = edge[1]
            cluster1 = DisjointSet.find(node1)
            cluster2 = DisjointSet.find(node2)
            if cluster1 == cluster2:
                continue
            else:
                return edge[0]
        

if __name__ == "__main__":
    
    GRAPH_PATH = 'Part2/test_files/clustering1.txt'
    graph = Graph.from_file(GRAPH_PATH)
    cluster_finder = ClusterFinder(graph)
    max_spacing = cluster_finder.find_max_spacing(4)
    print(max_spacing)
