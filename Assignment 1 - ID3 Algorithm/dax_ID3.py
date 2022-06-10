import argparse
from pathlib import Path
import math
from util import LearnTree


        
        
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
    

    # Getting training data from .dat file if path exists
    if args.train.exists() and args.train.is_file():
        # Looping thru file
        datapoints = []
        class_values = []
        with args.train.open() as f:
            for idx, line in enumerate(f):
                if idx == 0:
                    data = line.split()
                    num_attr = len(data) - 1
                    # print("Attribute columns: ", num_attr)
                    attr_names = data[:num_attr] # Getting first attr up to last
                    # print("Attributes: ", attr_names)
                else:
                    # Get data vectors that correspond to attributes and class(yes/no)
                    data = line.split()
                    datapoints.append(data[:num_attr]) # Creates vector list
                    class_values.append(data[-1]) # Creates class values list
                    
        # Create ID3 tree instance
        lt = LearnTree(attr_names, datapoints, class_values)
        
        # Create the tree with the training data
        lt.create_tree()
        
        # Print tree to stdout
        
                        

        # print("Training vectors list: ", datapoints)
        # print("Class values list: ", class_values)  

    else:
        print("Please provide a .dat file that exists. Make sure you are not just providing a directory.")
        exit()
        
    
    

    
    
if __name__ == '__main__':
    main()