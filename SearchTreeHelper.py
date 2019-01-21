class Node:
    def __init__(self, key):
        self._key = key
        self._parent = None
        self._left_child = None
        self._right_child = None

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, val):
        self._key = val

    @property
    def parent(self):
        return self._parent
    
    @parent.setter
    def parent(self, node):
        self._parent = node

    @property
    def left_child(self):
        return self._left_child
    
    @left_child.setter
    def left_child(self, node):
        self._left_child = node
    
    @property
    def right_child(self):
        return self._right_child
    
    @right_child.setter
    def right_child(self, node):
        self._right_child = node

    def swap(self, node):
        temp_parent = node.parent
        temp_left_child = node.left_child
        temp_right_child = node.right_child
        temp_key = node.key

        node.parent = self.parent
        node.key = self.key
        node.left_child = self.left_child
        node.right_child = self.right_child

        self.parent = temp_parent
        self.key = temp_key
        self.right_child = temp_right_child
        self.left_child = temp_left_child
        

    def is_left_child(self):
        return self.parent and self.parent.left_child == self
    
    def is_right_child(self):
        return self.parent and self.parent.right_child == self
    
    def is_root(self):
        return self._parent == None

class BinarySearchTree:
    def __init__(self):
        self._root = None
        self._size = 0

    @property
    def size(self):
        return self._size

    def insert(self, node):
            if self._root == None:
                self._root = node
            else:
                next_node = self._root
                while next_node:
                    if node.key <= next_node.key:
                        previous_node = next_node
                        next_node = previous_node.left_child
                    else:
                        previous_node = next_node
                        next_node = previous_node.right_child
                
                node.parent = previous_node
                if node.key <= previous_node.key:
                    previous_node.left_child = node
                else:
                    previous_node.right_child = node

            self._size += 1
        
    def find_min(self, node=None):
        if node is None:
            next_node = self._root
        else:
            next_node = node
        assert next_node, "Tree is empty."
        while next_node:
            retval = next_node.key
            next_node = next_node.left_child
        return retval

    def find_max(self, node=None):
        if node is None:
            next_node = self._root
        else:
            next_node = node
        assert next_node, "Tree is empty."
        while next_node:
            retval = next_node.key
            next_node = next_node.right_child
        return retval
    
    def search(self, key):
        next_node = self._root
        while next_node:
            if key < next_node.key:
                next_node = next_node.left_child
            elif key > next_node.key:
                next_node = next_node.right_child
            elif key == next_node.key:
                break
        if next_node is None:
            print("No such key in the tree!")
        return next_node
    
    def predecessor(self, node):
        if node.left_child:
            return self.find_max(node.left_child)
        else:
            current_node = node
            next_node = current_node.parent
            while not current_node.is_right_child() and not current_node.is_root():
                current_node = next_node
                next_node = current_node.parent
            if next_node is None:
                print('The node has no predecessor.')
            return next_node

    def delete(self, node):
        pass



if __name__ == "__main__":

    test_list = [2,4,5,4,6,2,7,1]
    tree = BinarySearchTree()
    for v in test_list:
        node = Node(v)
        tree.insert(node)
    print(tree.find_max())
    print(tree.find_min())
    print(tree.predecessor(node))
    


    
