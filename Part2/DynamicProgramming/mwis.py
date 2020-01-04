from typing import Dict, List, Tuple, Set

class MWISFinder:
    
    @staticmethod
    def find_max_weights(vertices: Dict[int, float]) -> Dict[int, float]:
        solution = {0: 0} # Base case 1
        for i in vertices:
            if i == 1: # Base case 2
                solution[i] = vertices[i]
            else: # Induction
                solution[i] = max(
                    solution[i-1], solution[i-2] + vertices[i]
                    )
        
        return solution
    
    @staticmethod
    def reconstruct(max_weights: Dict[int, float]) -> Set[int]:
        i = len(vertices)
        mwis = set()
        while i > 0:
            if max_weights[i] == max_weights[i - 1]:
                i = i - 1
            else:
                mwis.add(i)
                i = i -2
        return mwis
        
    def find_mwis(self, vertices: Dict[int, float]) -> Tuple[float, Set[int]]:
        max_weights = self.find_max_weights(vertices)
        mwis = self.reconstruct(max_weights)
        return max_weights[len(vertices)], mwis
    
if __name__ == '__main__':
    
    with open(
        'C:/Users/Fenzhengrou/Documents/Algorithm_Stanford/algorithm_stanford/Part2/DynamicProgramming/mwis_test_1',
        'r'
    ) as test_file:
        n = int(test_file.readline())
        vertices = {
            i + 1: int(test_file.readline()) for i in range(n)
        }
    max_weight, mwis = MWISFinder().find_mwis(vertices)
    
    print(f'The MWIS contains these vertices: {mwis}.\nIts weight is {max_weight}.')
    
    
                