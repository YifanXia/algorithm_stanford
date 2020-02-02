from __future__ import annotations
from typing import List, Dict, Tuple

class Node:
    
    def __init__(self, value: int, upstream: Node = None):
        self.value = value
        if not upstream:
            self.upstream = self
        else:
            self.upstream = Node
        self.set_size = 1
        
    def attach_upstream(self, other: Node):
        self.upstream = other
    
    def __repr__(self):
        return f'Node({self.value})'
        
    def __hash__(self):
        return hash(self.value)
    
    def __eq__(self, other: Node) -> bool:
        return self.value == other.value

class Graph:
    
    def __init__(self, nodes: List[Node], edges: List[Tuple[int, Tuple[Node, Node]]]):
        self.nodes = nodes
        self._adjacency_list = edges
    
    @classmethod
    def from_file(cls, path: str) -> Graph:
        nodes = []
        edges = []
        with open(path, 'r') as f:
            num_nodes, _ = [int(n) for n in f.readline().split()]
            nodes = [Node(i + 1) for i in range(num_nodes)]
            line = f.readline()
            while line:
                node1_id, node2_id, weight = [int(v) for v in line.split()]
                node1, node2 = nodes[node1_id - 1], nodes[node2_id - 1]
                edges.append(
                    (weight, (node1, node2))
                )
                line = f.readline()
        return cls(nodes, edges)
    
class DisjointSet:
    
    def __init__(self, graph: Graph):
        self.nodes = graph.nodes
    
    def make_set(self, nodes: List[str]):
        self.nodes = [Node(node_id) for node_id in nodes]
    
    @staticmethod
    def find(node: Node) -> Node:
        current_node = node
        upstream_node = node.upstream
        while upstream_node is not current_node:
            current_node = upstream_node
            upstream_node = upstream_node.upstream
        node.attach_upstream(current_node)
        return current_node
    
    @staticmethod
    def union(u: Node, v: Node) -> None:
        """Unite two sets: u and v
        
        Arguments:
            u {Node} -- Parent node of one set
            v {Node} -- Parent node of the other set
        """
        # Make u the upstream node of v
        if v.set_size <= u.set_size:
            v.attach_upstream(u)
            u.set_size += v.set_size
        else:
            u.attach_upstream(v)
            v.set_size += u.set_size
        
class KruskalSolver:
    
    def __init__(self, graph: Graph):
        self.graph = graph
        self.disjoint_set = DisjointSet(graph)
        self.set_size = 0
        self.mst_weight = 0
    
    def run_union_find(self, edge: List[Tuple[int, Tuple[Node, Node]]]):
        edge_weight = edge[0]
        node1, node2 = edge[1]
        set1 = DisjointSet.find(node1)
        set2 = DisjointSet.find(node2)
        if set1 == set2:
            pass
        else:
            self.mst_weight += edge_weight
            self.set_size = set1.set_size + set2.set_size
            DisjointSet.union(set1, set2)
    
    def run_kruskal(self):
        edges = sorted(self.graph._adjacency_list, key=lambda e: e[0])
        while self.set_size < len(self.graph.nodes):
            edge = edges.pop(0)
            self.run_union_find(edge)

if __name__ == "__main__":
    
    GRAPH_PATH = 'C:/Users/Fenzhengrou/Documents/Algorithm_Stanford/algorithm_stanford/Part2/test_files/mst_tests/test_mst_5.txt'
    graph = Graph.from_file(GRAPH_PATH)
    kruskal_solver = KruskalSolver(graph)
    kruskal_solver.run_kruskal()
    print(kruskal_solver.mst_weight)