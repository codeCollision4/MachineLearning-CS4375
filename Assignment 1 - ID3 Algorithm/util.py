import math
from collections import Counter

class Node():
    def __init__(self):
        self.next = None # Next branch in sequence of traversal
        self.children = None
        self.cls_val = None
        self.attr_name = None

class LearnTree():
    def __init__(self, attr_names, datapoints, class_values):
        '''
        Setup of data that algorithm uses
        '''
        self.attr_names = attr_names # List of attr names
        self.datapoints = datapoints # List of tuple/vectors/lists that hold binary attribute values
        self.class_values = class_values # List of class values of each datapoint
        self.training_class_count = [list(self.class_values).count(val) for val in list(set(self.class_values))] # Should return num of 0s and 1s in class values
        self.datapoint_ids = [line for line in range(len(self.datapoints))]
        self.sys_ent = self._get_entropy(self.datapoint_ids)
        self.attr_ids = [name_id for name_id in range(len(self.attr_names))]
        self.root = Node() # To start the tree
        
    def create_tree(self):
        '''
        Algorithm that will run the ID3 algorithm aka a decision tree that uses information gain and entropy to make a choice.
        '''
        
        # Call recursive helper which is the actual algorithm, start at root node. 
        self.root = self._id3(self.datapoint_ids, self.attr_ids, self.root) # Pass all datapoint ids, attribute ids and the root of tree to start creation
    
    def _id3(self, data_ids, attr_ids, node):
        # Actual algorithm here
        
        # data_ids is X in given alg

        # Gives Nonetype error if not present
        if not node:
            node = Node()
        
        # Class values of given data points, index links value to datapoint by id
        class_val_list = [self.class_values[id] for id in data_ids] # Y in given alg
        
        # Checking for pure node
        if len(set(class_val_list)) == 1:
            node.cls_val = class_val_list[0] # Since all class values are same any of them can be used
            return node
        
        # Checking if all data has same attribute value, the ids passed in will be zero if no more
        if len(attr_ids) == 0:
            # Getting majority if leaf node, no attributes left, non equal split among classes
            count = Counter(class_val_list)
            majority = count.most_common(1)[0][0]
            class_count = [class_val_list.count(val) for val in set(class_val_list)]
            
            # Checking if remaining classes have equal count
            if len(set(class_count)) == 1:
                temp = Counter(self.training_class_count)
                majority = temp.most_common(1)[0][0] # Tiebreak using training set majority
            
            # Set class value for node and then return
            node.cls_val = majority
            return node
        
        # Find attribute that gives highest info gain
        most_info_gain_attr = self._get_max_info_gain(attr_ids, data_ids)
        
        # Give node name of high ig attr
        node.attr_name = self.attr_names[most_info_gain_attr]
        
        # Create a child node for each value of attr after creating a list of all values the attr has
        attr_unique = [self.datapoints[id][most_info_gain_attr] for id in data_ids]
        node.children = [] # Create a list of nodes that are the children of this node, for multivalue attributes
        
        # Loop thru unique values and create a child node for it
        for val in list(set(attr_unique)):
            
            # Get child data ids
            child_data_ids = []
            for id in data_ids:
                if self.datapoints[id][most_info_gain_attr] == val:
                    child_data_ids.append(id)
            
            # Remove attribute from list, with a check that there are attr to remove from and that the highest gainer is in the list
            if len(attr_ids) != 0:
                if most_info_gain_attr in attr_ids:
                    attr_ids.remove(most_info_gain_attr)
            
            # Create node as a child
            child = Node()
            node.children.append(child) # Connect parent to child
            
            # Recursive call to continue to create tree
            child.next = self._id3(child_data_ids, attr_ids, child.next)
        
        # Returns tree
        return node
    
    def _get_max_info_gain(self, attr_ids, data_ids):
    
        # Get info gain for each attribute in list
        attr_ig = [self._get_info_gain(id, data_ids) for id in attr_ids]
        
        # Get max values attr id
        max_ig = attr_ids[attr_ig.index(max(attr_ig))]
        
        # Return the attr id 
        return max_ig
    
    def _get_info_gain(self, attr_id, data_ids):
        
        # Create a list of the chosen attributes values based on given datapoints
        attr_list = [self.datapoints[id][attr_id] for id in data_ids]
        
        # Get the count of 0s and 1s
        attr_count = [attr_list.count(val) for val in list(set(attr_list))]
        
        # Split ids of datapoints into proper attribute value
        attr_val_id = []
        for val in attr_count:
            unique_list = []
            for id in attr_list:
                if id == val:
                    unique_list.append(data_ids[id])
            attr_val_id.append(unique_list) # Create a list holding lists of ids for each attribute value
        
        
        # Calc the info gain
        ig = 0.00
        for val, ids in zip(attr_count, attr_val_id):
            ig = ig + -(val) / len(data_ids) * self._get_entropy(ids)
        
        # Returns Entropy of system minus entropy given a feature H(S) - H(S | Feature)
        return self.sys_ent - ig

    # Function to get entropy
    def _get_entropy(self, data_ids):
        
        # Total data points used
        total = len(data_ids)
        
        # Get the class value for each datapoint passed in, creates a list based that holds class values with the index corresponding to the data point id
        filtered_class_vals = [self.class_values[id] for id in data_ids]
        
        # Get a count for how many 0s and 1s for split
        split_count = [filtered_class_vals.count(cls_val) for cls_val in list(set(filtered_class_vals))]
        
        # Get entropy
        ent = 0.00
        for cls_val in split_count:
            ent = ent + -(cls_val / total) * math.log(cls_val / total, 2)
        
        return ent
    
    
    
    def print_tree(self):
        pass
    
    

        