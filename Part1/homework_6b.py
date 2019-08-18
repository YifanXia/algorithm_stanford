from SearchTreeHelper import Node, BinarySearchTree

if __name__ == '__main__':

    tree = BinarySearchTree()
    median_sum = 0
    with open('Median.txt', 'r') as f:
        k = 0
        line = f.readline()
        while line:
            node = Node(int(line))
            k += 1
            tree.insert(node)
            index = (k + 1) // 2
            median = tree.select(index).key
            median_sum += median
            line = f.readline()
            
    
    print(median_sum % k)
    """
    Correct answer: 1213
    """
