import argparse
from pathlib import Path
import math
import pandas as pd
import numpy as np

  
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
        train_vec = []
        class_val_vec = []
        with args.train.open() as f:
            # Read in file as DataFrame
            table = pd.read_csv(f, delim_whitespace=True)

        # Setting System Entropy
        # lt.set_sys_ent()
        
        # Creating ID3 Tree
        # lt.create_tree_id3(lt.train_vectors, lt.class_value_vector)

    else:
        print("Please provide a .dat file that exists. Make sure you are not just providing a directory.")
        exit()
        
    
    

    
    
if __name__ == '__main__':
    main()