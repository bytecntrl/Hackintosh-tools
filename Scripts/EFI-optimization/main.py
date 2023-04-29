import sys

from optimization import Optimization


def main():
    if (len(sys.argv) < 2):
        print("You have to put the path to the config!")
        sys.exit(1)

    op = Optimization(sys.argv[1])

    op.run()


if __name__ == "__main__":
    main()
