from typing import Set, List
from functools import total_ordering
import heapq

@total_ordering
class Node:
    def __init__(self, symbol: Set[str], frequency: int):
        self.symbol = symbol
        self.frequency = frequency
        
    def __lt__(self, other):
        return self.frequency < other.frequency
    
    def __eq__(self, other):
        return self.frequency == other.frequency
    
def get_initial_forest(path: str) -> List[Node]:
    with open(path, 'r') as file:
        num_nodes = int(file.readline())
        freqs = file.readlines()
        forest = [
            Node(symbol=[str(s)], frequency=int(freqs[s].strip())) for s in range(num_nodes)
        ]
        heapq.heapify(forest)
    return forest

class HuffmanEncoder:
    def __init__(self, forest: List[Node]):
        self.forest = forest
        self.encoding = {node.symbol[0]: '' for node in forest}
        self.frequencies = {node.symbol[0]: node.frequency for node in forest}
    
    def get_encoding(self):
        while len(self.forest) > 1:
            self.merge()
            
    def merge(self):
        left_tree = heapq.heappop(self.forest)
        right_tree = heapq.heappop(self.forest)
        for symbol in left_tree.symbol:
            self.encoding[symbol] += '0'
        for symbol in right_tree.symbol:
            self.encoding[symbol] += '1'
        new_root = Node(
            left_tree.symbol + right_tree.symbol,
            left_tree.frequency + right_tree.frequency,
        )
        heapq.heappush(self.forest, new_root)
            
    

if __name__ == "__main__":
    
    PATH = 'C:/Users/Fenzhengrou/Documents/Algorithm_Stanford/algorithm_stanford/Part2/GreedyAlgorithms/huffman_test_3'
    forest = get_initial_forest(PATH)
    
    huffman_encoder = HuffmanEncoder(forest)
    huffman_encoder.get_encoding()
    print(huffman_encoder.encoding)
    encoding_lengths = [len(code) for code in huffman_encoder.encoding.values()]
    print(min(encoding_lengths), max(encoding_lengths))
        