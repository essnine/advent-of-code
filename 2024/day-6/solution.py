import sys


def solve(lines: tuple[str, ...]):
    ...


def main(input_filename="input.txt"):
    lines = tuple(i.strip() for i in open(input_filename).readlines() if len(i))
    solve(lines)


if __name__ == "__main__":
    input_filename = "input.txt"
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            input_filename = "sample_input.txt"
    main(input_filename)
