import argparse

def __main__():
    parser = argparse.ArgumentParser(
            "echo", description="echo unix command"
        )
    
    parser.add_argument("strings", nargs="+", help="omit trailing newlines")
    parser.add_argument(
        "-n", action="store_true", help=""
    )
    args = parser.parse_args()

    output = " ".join(args.strings)
    if args.n:
        print(output, end="")
    else:
        print(output)


__main__()