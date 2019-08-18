class Node:
    def __init__(self, key):
        self._key = key
        self._parent = None
        self._left_child = None
        self._right_child = None
        self._tree_size = 1 # the size of the tree rooted at this node

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

    @property
    def tree_size(self):
        return self._tree_size
    
    def tree_size_increment(self):
        self._tree_size += 1
    
    def tree_size_decrement(self):
        self._tree_size -= 1

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
    def __init__(self, root=None):
        self._root = root
        if root is None:
            self._size = 0
        else:
            self._size = root._tree_size

    @property
    def size(self):
        return self._size

    def insert(self, node):
            if self._root == None:
                self._root = node
                self._size = node._tree_size
            else:
                next_node = self._root
                while next_node:
                    next_node.tree_size_increment()
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
            retval = next_node
            next_node = next_node.left_child
        return retval

    def find_max(self, node=None):
        if node is None:
            next_node = self._root
        else:
            next_node = node
        assert next_node, "Tree is empty."
        while next_node:
            retval = next_node
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

    def delete(self, key):
        node_to_delete = self.search(key)
        if node_to_delete is None:
            return
        else:
            next_parent = node_to_delete.parent
            while next_parent:
                next_parent.tree_size_decrement()
                next_parent = next_parent.parent
            if not node_to_delete.left_child and not node_to_delete.right_child:
                if node_to_delete.is_left_child():
                    node_to_delete.parent.left_child = None
                elif node_to_delete.is_right_child():
                    
                    node_to_delete.parent.right_child = None
            elif node_to_delete.left_child and node_to_delete.right_child:
                predecessor_node = self.predecessor(node_to_delete)
                node_to_delete.swap(predecessor_node)
                if predecessor_node.is_left_child():
                    predecessor_node.parent.left_child = None
                elif predecessor_node.is_right_child():
                    predecessor_node.parent.right_child = None
            elif node_to_delete.left_child and not node_to_delete.right_child:
                if node_to_delete.is_left_child():
                    node_to_delete.parent.left_child = node_to_delete.left_child
                elif node_to_delete.is_right_child():
                    node_to_delete.parent.right_child = node_to_delete.left_child
            elif not node_to_delete.left_child and node_to_delete.right_child:
                if node_to_delete.is_left_child():
                    node_to_delete.parent.left_child = node_to_delete.right_child
                elif node_to_delete.is_right_child():
                    node_to_delete.parent.right_child = node_to_delete.right_child
        
        self._size -= 1
    
    def select(self, index):
        if self._root.left_child:
            left_subtree_size = self._root.left_child.tree_size
        else:
            left_subtree_size = 0
        if index == left_subtree_size + 1:
            return self._root
        elif index < left_subtree_size + 1:
            subtree = BinarySearchTree(self._root.left_child)
            return subtree.select(index)
        elif index > left_subtree_size + 1:
            subtree = BinarySearchTree(self._root.right_child)
            return subtree.select(index-left_subtree_size-1)


            



if __name__ == "__main__":

    test_list = [2,4,5,4,6,2,7,1]
    tree = BinarySearchTree()
    for v in test_list:
        node = Node(v)
        tree.insert(node)
    print(tree.find_max().key)
    print(tree.find_min().key)
    print(tree.predecessor(node))
    nodee = tree.search(6)
    print(nodee.tree_size)
    root = tree._root
    print(root.tree_size)
    tree.delete(7)
    print(tree.size)
    print(tree.find_max().key)
    nodee = tree.search(6)
    print(nodee.tree_size)
    root = tree._root
    print(root.tree_size)
    s = tree.select(4)
    print(s.key)

    

    