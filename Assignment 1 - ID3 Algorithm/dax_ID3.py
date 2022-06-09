import argparse
from pathlib import Path


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
        with args.train.open() as f:
            for idx, line in enumerate(f):
                pass
    else:
        print("Please provide a .dat file that exists. Make sure you are not just providing a directory.")
        exit()
        
        
        
def id3(X, Y):
    '''
    Algorithm that will run the ID3 algorithm aka a decision tree that uses information gain and entropy to make a choice.
    '''
    
    