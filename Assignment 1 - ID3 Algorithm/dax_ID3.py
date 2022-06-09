import argparse
from pathlib import Path
import re

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
        
    def get_train_data(self, idx, line):
        # Get attribute and class names on first line
        if idx == 0:
            data = line.split()
            self.num_attr = len(data) - 1
            # print("Attribute columns: ", self.num_attr)
            self.attr_names = data[:self.num_attr] # Getting first attr up to last
            self.cls_name = data[-1] # Getting class value which is last in columns on line
            # print("Attributes: ", self.attr_names)
            # print("Class Name: ", self.cls_name)
        else:
            # Get data vectors that correspond to attributes and class(yes/no)
            data = line.split()
            self.train_vectors.append(data[:self.num_attr]) # Creates vector list
            self.class_value_vector.append(data[-1]) # Creates class values list
        

        
    def create_tree_id3():
        '''
        Algorithm that will run the ID3 algorithm aka a decision tree that uses information gain and entropy to make a choice.
        '''
        pass

    def test_id3():
        pass


        
        
def main():

    # Command Line Parser
    parser = argparse.ArgumentParser()

    # Positional Arguments
    parser.add_argument("train",
                        help="Path to a .dat file that holds training data",
                        type=Path
                        )
    parser.add_argument("test",
                        help="Path to a .dat file that holds test data",
                        type=Path
                        )
    # Parse input
    args = parser.parse_args()
    
    # Create LearnTree instance
    lt = LearnTree()

    # Getting training data from .dat file if path exists
    if args.train.exists() and args.train.is_file():
        # Looping thru file
        with args.train.open() as f:
            for idx, line in enumerate(f):
                # Funciton that parses data for training tree
                lt.get_train_data(idx, line)
            
            # print("Training vectors list: ", lt.train_vectors)
            # print("Class values list: ", lt.class_value_vector)
            
        # Creating ID3 Tree
        lt.create_tree_id3()   

    else:
        print("Please provide a .dat file that exists. Make sure you are not just providing a directory.")
        exit()
        
    
    
    # 
    
    
if __name__ == '__main__':
    main()