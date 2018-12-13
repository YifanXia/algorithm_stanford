#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  2 21:49:41 2018

@author: yifan
"""

from random import randint

class Graph:
    
    def __init__(self, graph_file):
        self._graph = {}
        self._num_edges = 0
        with open(graph_file) as file:
            for line in file:
                vertices = list(map(int, line.split()))
                vertex = vertices[0]
                neighbours = vertices[1:]
                self._graph[vertex] = [(vertex, n) for n in neighbours]
                self._num_edges += len(neighbours)
        self._num_edges = int(self._num_edges / 2)
    
    def get_number_of_edges(self):
        return self._num_edges
        
    def contraction(self, vertex_a, vertex_b):
        #print((vertex_a, vertex_b))
        #print(self._graph[vertex_a])
        #print(self._graph[vertex_b])
        vertex_new = vertex_a # the resulting vertex's id is the first of the two
        
        neighbours_a = [t for t in self._graph[vertex_a] if t != (vertex_a, vertex_b)] # remove the contracted edge
        neighbours_b = [t for t in self._graph[vertex_b] if t != (vertex_b, vertex_a)] # and parallel edges
        #neighbours_new = [(vertex_new, t[1]) for t in neighbours_a] +  [(t[0], vertex_new) for t in neighbours_b]
        neighbours_new = [(vertex_new, t[1]) for t in neighbours_a + neighbours_b]
        #print(neighbours_new)
        # Update the number of remaining edges
        delta_num_edges = len(self._graph[vertex_a] + self._graph[vertex_b]) - len(neighbours_a + neighbours_b)
        self._num_edges -= int(delta_num_edges / 2)
        
        # Update edge numbers
        for vb, vertex in self._graph[vertex_b]:
            #print(vb)
            #print(vertex)
            self._graph[vertex].remove((vertex, vb))
            self._graph[vertex].append((vertex, vertex_new))
            
        # Removed vertices to be merged
        self._graph.pop(vertex_a)
        self._graph.pop(vertex_b)
        
        # Add the resulting vertex
        self._graph[vertex_new] = neighbours_new
        #print(self._graph[vertex_new])
        
    def random_edge_choice(self):
        
        index = randint(0, self._num_edges-1)
        list_of_edges = [edge for neighbours in list(self._graph.values()) for edge in neighbours]
        #return list(self._graph.values())[index]
        #print(index)
        #print(len(list_of_edges))
        return list_of_edges[index]
    
    def karger_min_cut(self):
        while len(self._graph) > 2:
            vertex_a, vertex_b = self.random_edge_choice()
            self.contraction(vertex_a, vertex_b)
            
def find_min_cut(num_calls, graph_file_name):
    num_edges_cut = []
    for i in range(num_calls):
        graph = Graph(graph_file_name)
        #print(graph._graph[187'])
        graph.karger_min_cut()
        
        num_edges_cut.append(graph.get_number_of_edges())
        if i%100 ==0:
            print("{}th call of Karger min cut".format(i))
            print(min(num_edges_cut))
    return num_edges_cut

if __name__ == '__main__':
    import math
    
    cuts = find_min_cut(int(200*200*math.log2(200)), "kargerMinCut.txt")
    print(min(cuts))
            