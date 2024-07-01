import argparse
import logging
import os


def check_file_error(filepath):
    if not os.path.exists(filepath):
        logging.error(f"Incorrect file path or file does not exist: {filepath}")



def __main__():
    parser = argparse.ArgumentParser(
        "head", description="wc unix command"
    )
    
    parser.add_argument("-l", action="store_true", help="Print Number of lines")
    parser.add_argument("-w", action="store_true", help="Print Number of words")
    parser.add_argument("-c", action="store_true", help="Print Number of characters")
    parser.add_argument('filepath', type=str, help='path to the file')
    args = parser.parse_args()
    if not args.filepath:
            logging.error("No file passed")
            raise FileNotFoundError("No file passed")
    filePath = args.filepath
    check_file_error(filePath)


    lineCount = 0
    wordCount = 0
    charactersCount = 0
    with open(filePath, encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            lineCount += 1
            words = line.split(' ')
            wordCount += len(words)
            charactersCount += len(line)

    
    if args.l:
        print(lineCount)
    if args.w:
        print(wordCount)
    if args.c:
        print(charactersCount)
    


__main__()