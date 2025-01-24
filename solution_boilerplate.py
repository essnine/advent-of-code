def solve(lines: tuple[str, ...]):
    ...


def main():
    lines = tuple(i.strip() for i in open("input.txt").readlines())
    solve(lines)


if __name__ == "__main__":
    main()
