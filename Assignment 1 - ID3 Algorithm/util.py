import math

class Node():
    def __init__(self):
        self.next = None # Next branch in sequence of traversal
        self.branches = None # Nodes that branch off
        self.data = None # Either the feature we used to split or the class value that is returned as a leaf

class LearnTree():
    def __init__(self, attr_names, datapoints, class_values):
        '''
        Setup of data that algorithm uses
        '''
        self.attr_names = [] # List of attr names
        self.datapoints = [] # List of tuple/vectors/lists that hold binary attribute values
        self.class_values = class_values # List of class values of each datapoint
        self.sys_ent = self._get_entropy(class_values)
        self.root = None

        
    def create_tree(self):
        '''
        Algorithm that will run the ID3 algorithm aka a decision tree that uses information gain and entropy to make a choice.
        '''
        
        # Call recursive helper which is the actual algorithm, start at root node
        self.root = self._id3(self.datapoints, self.class_values, self.root)
    
    def _id3(self, datapoints, class_values, node):
        # Actual algorithm here
        pass
    
    # Boolean function that will return whether all training vectors have same class value
    def _is_same_cls(self, cv):
        return len(set(cv)) == 1
    
    # Function to get entropy
    def _get_entropy(self, vec):
        no = vec.count("0")
        yes = vec.count("1")
        total = no + yes
        # print(f"Split: no {no} , yes {yes}")
        # print(f"Total: {total}")
        
        ent = -(no / total) * math.log(no / total, 2) + -(yes / total) * math.log(yes / total, 2)
        # print(ent)
        
        return ent

        
        

    def test_id3():
        pass
