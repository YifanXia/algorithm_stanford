from typing import Set, List
from functools import total_ordering
import heapq

@total_ordering
class Node:
    
    def __init__(self, symbol, frequency, left = None, right = None):
        
        self._0 = left
        self._1 = right
        self.symbol = symbol
        self.frequency = frequency
        
    def __lt__(self, other):
        return self.frequency < other.frequency
    
    def __eq__(self, other):
        return self.frequency == other.frequency
        
    
    
def gather_forest(path: str) -> List[Node]:
    with open(path, 'r') as file:
        num_nodes = int(file.readline())
        freqs = file.readlines()
        forest = [
            Node(symbol=str(s), frequency=int(freqs[s].strip())) for s in range(num_nodes)
        ]
        heapq.heapify(forest)
    return forest

class HuffmanEncoder:
    pass

if __name__ == "__main__":
    
    PATH = 'C:/Users/Fenzhengrou/Documents/Algorithm_Stanford/algorithm_stanford/Part2/GreedyAlgorithms/huffman_test_2'
    forest = gather_forest(PATH)
    for tree in forest:
        print(tree.symbol, tree.frequency)
        