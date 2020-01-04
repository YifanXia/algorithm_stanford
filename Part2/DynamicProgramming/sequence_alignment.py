import sys
from typing import Tuple

class AlignmentFinder:
    
    def __init__(self, p_gap: int, p_miss: int, x_seq: str, y_seq: str):
        self.p_gap = p_gap
        self.p_miss = p_miss
        self._cache = {}
        self.min_nw = self.find_min_NW(x_seq, y_seq)
    
    def find_min_NW(self, x_seq: str, y_seq: str) -> int:
        current_key = (len(x_seq), len(y_seq))
        if current_key in self._cache:
            return self._cache[current_key]
        if not x_seq:
            self._cache[current_key] = self.p_gap * len(y_seq)
        elif not y_seq:
            self._cache[current_key] = self.p_gap * len(x_seq)
        else:
            p_xy_tail = self.p_miss * (x_seq[-1] is not y_seq[-1])
            self._cache[current_key] = min(
                # Case 1: The last column of both sequences matches
                self.find_min_NW(x_seq[:-1], y_seq[:-1]) + p_xy_tail,
                # Case 2: The last column of x matches a gap in y
                self.find_min_NW(x_seq[:-1], y_seq) + self.p_gap,
                # Case 3: The last column of y matches a gap in x
                self.find_min_NW(x_seq, y_seq[:-1]) + self.p_gap,
            )
        return self._cache[current_key]
            
    
if __name__ == "__main__":
    
    sys.setrecursionlimit(3000)
    with open(
        'C:/Users/Fenzhengrou/Documents/Algorithm_Stanford/algorithm_stanford/Part2/DynamicProgramming/alignment_test',
        'r'
    ) as test_file:
        length_x, length_y = [int(n) for n in test_file.readline().split()]
        p_gap, p_miss = [int(n) for n in test_file.readline().split()]
        x_seq = test_file.readline().strip()
        y_seq = test_file.readline().strip()
    
    alignment_finder = AlignmentFinder(p_gap, p_miss, x_seq, y_seq)
    print(alignment_finder.min_nw)
    