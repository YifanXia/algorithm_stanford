from collections import namedtuple
from typing import List, Set, Dict, Tuple, Union
import sys

Item = namedtuple('Item', ['value', 'size'])

class KnapsackFinder:
    
    def __init__(self, items: List[Item], capacity: int):
        self._cache = {}
        self.value = self.recursive_find(items, capacity)
    
    @staticmethod
    def find_solutions(items: List[Item], capacity: int) -> Dict[Tuple[int, int], int]:
        solutions = {}
        for i in range(len(items) + 1):
            if i % 10 == 0:
                print(f'Item No. {i}...')
            for c in range(capacity + 1):
                if i * c == 0:
                    continue#solutions[(i, c)] = 0
                elif items[i - 1].size > c:
                    continue
                else:
                    item_size = items[i - 1].size
                    item_value = items[i - 1].value
                    solutions[(i, c)] = max(
                        solutions.get((i - 1, c - item_size), 0) + item_value,
                        solutions.get((i - 1, c), 0)
                    )
        return solutions
    
    def recursive_find(self, items: List[Item], capacity: int) -> Union[float, int]:
        """Find the solution recursively when the test case is too big
        
        Arguments:
            items {List[Item]} -- [description]
            capacity {int} -- [description]
        
        Returns:
            Union[float, int] -- [description]
        """
        current_key = (len(items), capacity)
        if current_key in self._cache:
            return self._cache[current_key]
        if not items or capacity == 0:
            self._cache[current_key] = 0
        elif items[-1].size > capacity:
            self._cache[current_key] = self.recursive_find(items[:-1], capacity)
        else:
            current_item = items[-1]
            solution_w_current_item = self.recursive_find(items[:-1], capacity - current_item.size) + current_item.value
            solution_wo_current_item = self.recursive_find(items[:-1], capacity)
            self._cache[current_key] = max(solution_w_current_item, solution_wo_current_item)
        return self._cache[current_key]
            
def parse_item(string: str) -> Item:
    value, size = [int(x) for x in string.split()]
    return Item(value, size)

if __name__ == "__main__":
    
    sys.setrecursionlimit(3000)
    with open(
        'C:/Users/Fenzhengrou/Documents/Algorithm_Stanford/algorithm_stanford/Part2/DynamicProgramming/knapsack_test_2',
        'r'
    ) as test_file:
        knapsack_capacity, items_number = [int(x) for x in test_file.readline().split()]
        items = [parse_item(test_file.readline()) for _ in range(items_number)]
    knapsack_finder = KnapsackFinder(items, knapsack_capacity)
    print(knapsack_finder.value)
    