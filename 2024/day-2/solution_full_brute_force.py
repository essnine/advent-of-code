from itertools import pairwise
from pprint import pprint


def solve(lines):
    count_safe = 0
    count_check_safe = 0

    for line_num, report in enumerate(lines):
        level_list = list(map(int, report.split()))
        if is_safe(level_list):
            count_safe += 1
        else:
            for i, _ in enumerate(level_list):
                levels_copy = level_list.copy()
                levels_copy.pop(i)
                if is_safe(levels_copy):
                    count_check_safe += 1
                    break

    pprint(count_safe)
    pprint(count_check_safe)
    pprint(count_safe + count_check_safe)


def is_safe(levels: list) -> bool:
    fl_safe = False
    lev_steps = list(pairwise(levels))
    steps = [(b - a) for a, b in lev_steps]

    step_sequence_check = False
    step_size_check = [bool(1 <= abs(k) <= 3) for k in steps]

    if all([i < 0 for i in steps]) or all([i > 0 for i in steps]):
        step_sequence_check = True

    if all(step_size_check):
        if step_sequence_check:
            fl_safe = True
    return fl_safe


def main():
    lines = tuple(i for i in open("input.txt").readlines())
    solve(lines)


if __name__ == "__main__":
    main()
