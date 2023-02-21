"""
Console application - CLI - Command Line Interface

"""
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--random', type=int, help="Create n random numbers")
    args = parser.parse_args()
    
    print(args.random)