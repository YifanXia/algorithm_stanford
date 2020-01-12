from typing import List
from collections import namedtuple

Node = namedtuple('Node', ['key', 'freq'])
inf = float('inf')

class BinarySearchTreeOptimizer:
    
    def __init__(self):
        pass
    
    def _iteratively_find_optimal_bst(self, nodes: List[Node]) -> float:
        num_nodes = len(nodes)
        
        self._cache = [
            [0 for _ in range(0, num_nodes + 2)] for _ in range(0, num_nodes + 2)
        ]
        # Base case: total weighted search time is zero when:
        #   1. number of nodes is 0; or
        #   2. key = 0 or 1
        for s in range(0, num_nodes):
            # Loop over all possible sizes of subproblem
            # As in DP, smaller subproblems need to be solved before bigger ones, we must
            # loop over sizes from 1 to num_nodes
            for i in range (1, num_nodes + 1 - s):
                # Loop over all possible starting index
                # End index j is i + s
                j = i + s
                sum_ps = sum(node.freq for node in nodes[i - 1:j])
                min_bst = min(
                    self._cache[i][r - 1] + self._cache[r + 1][j] for r in range(i, j + 1)
                )
                self._cache[i][i + s] = sum_ps + min_bst
        return self._cache[1][num_nodes]
    
def read_nodes(path: str) -> List[Node]:
    with open(path, 'r') as inputfile:
        num_nodes = int(inputfile.readline())
        freqs = inputfile.readline().split(',')
    
    return [Node(key, float(freqs[key])) for key in range(num_nodes)]

if __name__ == "__main__":
    
    optimal_bst_finder = BinarySearchTreeOptimizer()
    nodes = read_nodes('C:/Users/Fenzhengrou/Documents/Algorithm_Stanford/algorithm_stanford/Part2/DynamicProgramming/optimal_bst_test')
    min_search_time = optimal_bst_finder._iteratively_find_optimal_bst(nodes)
    
    print(min_search_time)
    