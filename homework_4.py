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
                try:
                    self.adjacency_list[start] = self.adjacency_list[start] + [fin]
                except KeyError:
                    self.adjacency_list[start] = [fin]
                
                try:
                    self.reverse_list[fin] = self.reverse_list[fin] + [start]
                except KeyError:
                    self.reverse_list[fin] = [start]
                

if __name__ == '__main__':

    input_file = "SCC.txt"
    graph = Graph()
    graph.read_input_file(input_file)


                
                


