class MinHeap:
    '''
    Define a MinHeap data structure from scratch.
    A MinHeap extracts the minimum value in logarithmic time
    '''
    def __init__(self):
        self.data = [] # a list to store data
        self.size = 0  # size of the heap

    def build_heap(self, input_list):
        self.size = len(input_list)
        self.data = input_list
        index_first_leaf = (self.size - 1) // 2
        #for i in range(index_first_leaf, self.size):
        #    self.min_heapify(i)
        # for i in range(index_first_leaf):
        #     self.max_heapify(i)
        i = index_first_leaf
        while i >= 0:
            self.max_heapify(i)
            i -= 1

    def min_heapify(self, index):
        index_par = (index - 1) // 2
        while self.data[index] < self.data[index_par]:
            temp = self.data[index]
            self.data[index] = self.data[index_par]
            self.data[index_par] = temp
            index = index_par
            index_par = max(0, (index - 1) // 2)
    
    def max_heapify(self, index):
        index_child = self.small_child(index)
        while self.data[index] > self.data[index_child]:
            temp = self.data[index]
            self.data[index] = self.data[index_child]
            self.data[index_child] = temp
            index = index_child
            if 2 * index + 1 < self.size:
                index_child = self.small_child(index)

    def insert(self, obj):
        self.data.append(obj)
        self.size += 1
        if self.size > 1:
            index_new = self.size - 1 # the index of the new object
            self.min_heapify(index_new)
            
    
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
            self.max_heapify(index_par)
        return retval

if __name__ == "__main__":

    #list_to_heap = [9, 4, 12, 9, 4, 4, 8, 11, 13]
    list_to_heap = [10,9,8,7,6,1,2,3,4,5]
    min_heap = MinHeap()
    for i in list_to_heap:
        min_heap.insert(i)
    print(min_heap.data)
    print(min_heap.size)
    for _ in range(len(list_to_heap)):
        heap_min = min_heap.extract_min()
        print('extracted {} from heap.'.format(heap_min))
        print('remaining heap {}.'.format(min_heap.data))
    
    new_min_heap = MinHeap()
    new_min_heap.build_heap(list_to_heap)
    print(new_min_heap.data)
    for _ in range(len(list_to_heap)):
        heap_min = new_min_heap.extract_min()
        print('extracted {} from heap.'.format(heap_min))
        print('remaining heap {}.'.format(new_min_heap.data))
    

