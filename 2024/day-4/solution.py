import re
import sys


def solve(lines: tuple[str, ...]):
    rows = [i.strip() for i in lines]
    raw_rows = [list(i) for i in lines]
    count = 0
    raw_cols = list(zip(*raw_rows[::-1]))
    cols = ["".join(i) for i in raw_cols if i]

    _rows = scan(rows)
    print("_rows: ", _rows)
    count += _rows
    _cols = scan(cols)
    print("_cols: ", _cols)
    count += _cols
    _d_raw_rows = scan_d(raw_rows)
    print("_d_raw_rows: ", _d_raw_rows)
    count += _d_raw_rows
    _d_raw_cols = scan_d(raw_cols)
    print("_d_raw_cols: ", _d_raw_cols)
    count += _d_raw_cols
    print("count: ", count)
    x_mas_count = get_x_mas_count(raw_cols)
    print("x_mas_count: ", x_mas_count)


def scan(cross_grid: list[str]) -> int:
    row_match_count = 0
    for row in cross_grid:
        matches = re.findall(r"XMAS", row)
        row_match_count += len(matches)
        rev_matches = re.findall(r"SAMX", row)
        row_match_count += len(rev_matches)
    return row_match_count


def scan_d(cross_grid: list[list[str]]) -> int:
    lines = get_diagonal_scans(cross_grid)
    row_match_count = 0
    for row in lines:
        matches = re.findall(r"XMAS", row)
        row_match_count += len(matches)
        rev_matches = re.findall(r"XMAS", "".join(row[::-1]))
        row_match_count += len(rev_matches)
    return row_match_count


def get_diagonal_scans(cross_grid: list[list[str]]):
    scans = []
    y_init = 0
    y_max = len(cross_grid) - 1
    while y_init <= y_max:
        scan_buf = []
        rev_scan_buf = []
        x = 0
        y = y_init
        # print(f"For y: {y}")
        while y >= 0:
            # if y_init < 10:
                # print(
                #     f"\tX: {x}\tY: {y}\tcross_grid[{y}][{x}]:{cross_grid[y][x]}\t"
                #     f"cross_grid[{y_max - x}][{y_max - y}]:{cross_grid[y_max - x][y_max - y]}"
                # )
            scan_buf.append(cross_grid[y][x])  # scanning from the top down
            if (y_max - x,y_max - y) != (y, x):
                pass
                rev_scan_buf.append(
                    cross_grid[y_max - x][y_max - y]
                )  # scanning from the bottom up
            y -= 1
            x += 1
        scans.append("".join(scan_buf))
        scans.append("".join(rev_scan_buf))
        y_init += 1
    # print(scans)
    return scans


def get_x_mas_count(lines: list[list[str]]) -> int:
    count = 0
    for raw_line_idx, line in enumerate(lines[1:-1]):
        line_idx = raw_line_idx + 1
        for idx, val in enumerate(line[1:-1]):
            if val == "A":
                left_above = lines[line_idx-1][idx]
                left_below = lines[line_idx+1][idx]
                right_above = lines[line_idx-1][idx+2]
                right_below = lines[line_idx+1][idx+2]

                if ((left_above, val, right_below), (right_above, val, left_below)) in {
                    (("S", "A", "M"), ("S", "A", "M")),
                    (("M", "A", "S"), ("S", "A", "M")),
                    (("S", "A", "M"), ("M", "A", "S")),
                    (("M", "A", "S"), ("M", "A", "S")),
                }:
                    # print(idx)
                    count += 1
    return count


def main(input_filename="input.txt"):
    lines = tuple(i.strip() for i in open(input_filename).readlines() if len(i))
    solve(lines)


if __name__ == "__main__":
    input_filename = "input.txt"
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            input_filename = "sample_input.txt"
    main(input_filename)
