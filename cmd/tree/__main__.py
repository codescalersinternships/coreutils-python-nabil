import argparse
import os
import sys
import logging


def tree(currLevel, maxLevel, dirPath):
    if currLevel > maxLevel:
        return
    
    try:
        content = os.listdir(dirPath)
    except Exception as e:
        logging.error(f"Incorrect file path or file does not exist: {dirPath}")
    
    for entry in content:
        path = os.path.join(dirPath, entry)
        for i in range(1, currLevel):
            print(" ", end="")
        if os.path.isdir(path):
            print("|--", entry)
            tree(currLevel + 1, maxLevel, path)
        else:
            print("|--", entry)

def __main__():
    parser = argparse.ArgumentParser(description="tree unix command")
    parser.add_argument('-l', '--level', type=int, default=2, help='depth')
    parser.add_argument('dirpath', type=str, help='path to the directory')
    args = parser.parse_args()

    if not os.path.isdir(args.dirpath):
        sys.exit("No valid directory passed")

    tree(1, args.level, args.dirpath)

__main__()
