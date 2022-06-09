import math

class Node():
    def __init__(self):
        self.left = None # Yes branch
        self.right = None # No branch
        self.data = None # class value ie which class is returned by this node

class LearnTree():
    def __init__(self):
        '''
        Setup of data that algorithm uses
        '''
        self.attr_names = [] # List of names at top of training data
        self.cls_name = []  # Name of class to distinguish
        self.num_attr = 0   # Number of attributes training on
        self.train_vectors = [] # List of tuple/vectors/lists that hold binary attribute values
        self.class_value_vector = [] # List/vector that holds binary class value for each "line"/datapoints
        self.sys_ent = None
        self.root = None
        
        
        
    def set_sys_ent(self):
        self.sys_ent = self._get_entropy(self.class_value_vector)

        
    def create_tree_id3(self, train_vec, cls_vec, node):
        '''
        Algorithm that will run the ID3 algorithm aka a decision tree that uses information gain and entropy to make a choice.
        '''
        # If all data points in training vector has same class value return the node class choice
        if self._is_same_cls(train_vec, cls_vec):
            return node.data
    
    # Boolean function that will return whether all training vectors have same class value
    def _is_same_cls(self, cv):
        zeroes = cv.count("0")
        ones = cv.count("1")
        if zeroes or ones == 0:
            return True
        else:
            return False
    
    # Function to get entropy
    def _get_entropy(self, vec):
        zeroes = vec.count("0")
        ones = vec.count("1")
        total = zeroes + ones
        # print(f"Split: zeroes {zeroes} , ones {ones}")
        # print(f"Total: {total}")
        
        ent = -(zeroes / total) * math.log(zeroes / total, 2) + -(ones / total) * math.log(ones / total, 2)
        # print(ent)
        
        return ent
        
        

    def test_id3():
        pass
