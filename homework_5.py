class MinHeap:
    '''
    Define a MinHeap data structure from scratch.
    A MinHeap extracts the minimum value in logarithmic time
    '''
    def __init__(self):
        self.data = [] # a list to store data
        self.size = 0  # size of the heap

    def insert(self, obj):
        self.data.append(obj)
        self.size += 1
        if self.size > 1:
            index_new = self.size - 1 # the index of the new object
            index_par = (index_new - 1) // 2 # the index of its direct parent
        
            # a while loop swapping parent-child position if child < parent
            while self.data[index_new] < self.data[index_par]:
                temp = self.data[index_new]
                self.data[index_new] = self.data[index_par]
                self.data[index_par] = temp
                index_new = index_par
                index_par = max(0, (index_new - 1) // 2)
    
    def small_child(self, i):
        '''
        given an object of index i, returns the index of its small child
        '''
        if 2 * i + 3 > self.size:
            return 2 * i + 1
        else:
            if self.data[2 * i + 1] < self.data[2 * i + 2]:
                return 2 * i + 1
            else:
                return 2 * i + 2

    def extract_min(self):
        retval = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self.size -= 1
        index_par = 0
        if self.size > 1:
            index_child = self.small_child(index_par)
            while self.data[index_par] > self.data[index_child]:
                temp = self.data[index_par]
                self.data[index_par] = self.data[index_child]
                self.data[index_child] = temp
                index_par = index_child
                if 2 * index_par + 1 < self.size:
                    index_child = self.small_child(index_par)
        return retval

if __name__ == "__main__":

    list_to_heap = [9, 4, 12, 9, 4, 4, 8, 11, 13]
    min_heap = MinHeap()
    for i in list_to_heap:
        min_heap.insert(i)
    print(min_heap.data)
    print(min_heap.size)
    for _ in range(len(list_to_heap)):
        heap_min = min_heap.extract_min()
        print('extracted {} from heap.'.format(heap_min))
        print('remaining heap {}.'.format(min_heap.data))
    

