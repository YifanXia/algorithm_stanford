import sys
from collections import defaultdict
sys.setrecursionlimit(1000000)

class Graph:

    def __init__(self):
        self.adjacency_list = defaultdict(list)
        self.reverse_list = defaultdict(list)

    def read_input_file(self, file_name):
        print('Loading the graph...')
        with open(file_name, 'r') as f:
            for edge in f:
                end_points = list(map(int, edge.split()))
                assert(len(end_points) == 2)
                start = end_points[0]
                fin = end_points[1]
                #print(start)
                
                if start not in self.adjacency_list:
                    self.adjacency_list[start] = [fin]
                else:
                    self.adjacency_list[start].append(fin)
                if fin not in self.adjacency_list:
                    self.adjacency_list[fin] = []
                
                if fin not in self.reverse_list:
                    self.reverse_list[fin] = [start]
                else:
                    self.reverse_list[fin].append(start)
                if start not in self.reverse_list:
                    self.reverse_list[start] = []
                
        print("Graph Loaded.")
    
def get_nodes(adjacency_list):
    return adjacency_list.keys()

def get_neighbours(adjacency_list, v):
    return adjacency_list[v]
        
def DFS_visit(adjacency_list, vertex, parents, finished):
    #print(vertex)
    #print(parents)
    for v in get_neighbours(adjacency_list, vertex):
        if v not in parents:
            print("To visit node {}.".format(v))
            parents[v] = vertex
            DFS_visit(graph, v, parents, finished)
    
    finished.append(vertex)


def DFS_visit_iter(adjacency_list, vertex, visited, finished, ordered, num_nodes):
    stack = [vertex]
    while len(stack) != 0:
        #print(stack)
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            if len(visited) % 1000 == 0:
                print('{n1} vertices out of {n2} are visited.'.format(n1=len(visited), n2=num_nodes))
            stack.append(v)
            for w in get_neighbours(adjacency_list, v):
                if w not in visited:
                    stack.append(w)
        else:
            if v not in finished:
                ordered.append(v)
                finished.add(v)

def DFS_iter(adjacency_list):
    '''
    iterative DFS
    '''
    nodes = get_nodes(adjacency_list)
    num_nodes = len(nodes)
    finished = set()
    ordered = []
    visited = set()
    print('Starting iterative DFS')
    for vertex in nodes:
        if vertex not in finished:
            """ stack = [vertex]
            while len(stack) != 0:
                print(stack)
                v = stack.pop()
                if v not in visited:
                    visited.append(v)
                    if len(visited) % 1000 == 0:
                        print('{n1} vertices out of {n2} are visited.'.format(n1=len(visited), n2=num_nodes))
                    stack.append(v)
                    for w in get_neighbours(adjacency_list, v):
                        if w not in visited:
                            stack.append(w)
                else:
                    if v not in finished:
                        finished.append(v) """
            DFS_visit_iter(adjacency_list, vertex, visited, finished, ordered, num_nodes)

    print('DFS ends.')    
    return ordered




def DFS(adjacency_list):
    parents = {}
    finished = []
    print('Starting DFS')
    for v in get_nodes(adjacency_list):
        print('Processing node {}...'.format(v))
        if v not in parents:
            parents[v] = None
            DFS_visit(graph, v, parents, finished)
    return parents, finished


def find_SCCs(reversed_list, finished_DFS):
    finished_DFS.reverse()
    num_nodes = len(finished_DFS)
    visited = set()
    finished = set()
    ordered = []
    count_SCCs = 0
    num_counted_vertices = 0
    SCCs = defaultdict(set)
    print('Computing SCCs...')
    for vertex in finished_DFS:
        if vertex not in visited:
            count_SCCs += 1
            DFS_visit_iter(reversed_list, vertex, visited, finished, ordered, num_nodes)
            #print(visited)
            #print(set(visited))
            #print(set(temp_SCC))
            SCCs[count_SCCs] = len(visited) - num_counted_vertices
            num_counted_vertices = len(visited)
    print('SCCs completed.')
    return SCCs
                

if __name__ == '__main__':

    input_file = "SCC.txt"
    graph = Graph()
    graph.read_input_file(input_file)
    #parents, finished = DFS(graph)
    finished = DFS_iter(graph.adjacency_list)
    
    #print(finished)
    #print(visited)

    SCCs = find_SCCs(graph.reverse_list, finished)
    print('There are {} SCCs.'.format(len(SCCs)))
    print(sorted(SCCs.values(), reverse=True)[0:5])
    
    
