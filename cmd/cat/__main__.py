import argparse
import logging
import os

def check_file_error(filepath):
    if not os.path.exists(filepath):
        logging.error(f"Incorrect file path or file does not exist: {filepath}")


def __main__():
    parser = argparse.ArgumentParser(description="cat unix command")
    parser.add_argument('-n', action='store_true', help="number of lines")
    parser.add_argument('filepath', type=str, help='path to the file')
    args = parser.parse_args()


    if not args.filepath:
            logging.error("No file passed")
            raise FileNotFoundError("No file passed")
    filepath = args.filepath
    check_file_error(filepath)

    i: int = 1
    with open(filepath, encoding="utf-8") as fileReader:
        for line in fileReader:
            if args.n:
                print(i," ", line)
            else:
                print(line)
            print("\n")
            i += 1

__main__()