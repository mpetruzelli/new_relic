import sys
from phrases import top_ten


def main():
    try:
        if sys.stdin.isatty():
            if not sys.argv[1]:
                raise IndexError
    except IndexError:
        print("no stdin or file paths supplied")
        print("Usages: ")
        print(" phrases file1.txt file2.txt")
        print(" cat file2.txt | phrases")
    else:
        print("{}".format(top_ten.main()))


if __name__ == '__main__':
    main()
