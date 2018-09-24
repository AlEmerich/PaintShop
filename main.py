import argparse
from paintshop.process import get_optimal_set

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str)
    args = parser.parse_args()
    print(get_optimal_set(args.path))
