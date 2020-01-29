from __future__ import annotations
from typing import List, Dict, Tuple

class Node:
    
    def __init__(self, value: str, upstream: Node = None):
        self.value = value
        if not upstream:
            self.upstream = self
        else:
            self.upstream = Node
        
    def attach_upstream(self, other: Node):
        self.upstream = other
    
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
        nodes = set()
        edges = []
        with open(path, 'r') as f:
            _ = f.readline()
            line = f.readline()
            while line:
                node1_id, node2_id, weight = [v for v in line.split()]
                node1, node2 = Node(node1_id), Node(node2_id)
                nodes.add(node1),
                nodes.add(node2)
                edges.append(
                    (int(weight), (node1, node2))
                )
                line = f.readline()
        return cls(nodes, edges)
    
class DisjointSet:
    
    def __init__(self, graph: Graph):
        self.nodes = graph.nodes
    
    def make_set(self, nodes: List[str]):
        self.nodes = [Node(node_id) for node_id in nodes]
    
    def find(self, node: Node) -> Node:
        current_node = node
        upstream_node = node.upstream
        while upstream_node is not current_node:
            current_node = upstream_node
            upstream_node = upstream_node.upstream
        return current_node
    
    def union(self, u: Node, v: Node) -> None:
        """Unite two sets: u and v
        
        Arguments:
            u {Node} -- Parent node of the LARGER set
            v {Node} -- Parent node of the SMALLER set
        """
        v.attach_upstream(u)
        