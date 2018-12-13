class Graph:
    
    def __init__(self):
        self.adjacency_list = {}

    def read_input_file(self, file_name):
        with open(file_name, 'r') as f:
            for edge in f:
                end_points = list(map(int, edge.split()))
                assert(len(end_points) == 2)


