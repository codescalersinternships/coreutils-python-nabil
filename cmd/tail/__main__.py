import argparse
import logging
import os


def check_file_error(filepath):
    if not os.path.exists(filepath):
        logging.error(f"Incorrect file path or file does not exist: {filepath}")
def __main__():
    parser = argparse.ArgumentParser(
        "head", description="tail unix command"
    )
    parser.add_argument(
        "-n", type=int, help="number of lines", default=10
    )
    parser.add_argument('filepath', type=str, help='path to the file')
    args = parser.parse_args()
    if not args.filepath:
            logging.error("No file passed")
            raise FileNotFoundError("No file passed")
    filePath = args.filepath
    check_file_error(filePath)
    lines = []
    with open(filePath, encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            lines.append(line)
    if(len(lines) < args.n):
         logging.error(f"lines aren't enough")
    
    for i in range(len(lines) - (args.n),len(lines)):
            print(lines[i])

__main__()