import re


def only_mults(mem: str):
    op = 0
    instances = re.findall(r"mul\(\d{0,3},\d{0,3}\)", mem)
    for instance in instances:
        nums = list(map(int, instance[4:-1].split(",")))
        val = nums[0] * nums[1]
        op += val
    return op


def coded_mults(mem: str):
    toggle_map = {
        True: "don't()",
        False: "do()",
    }

    fl_toggle_do = True
    # mults = 0
    mult_acc = []

    while True:
        split_val = toggle_map[fl_toggle_do]
        split_mem = mem.split(split_val, 1)
        if len(split_mem) == 1:
            break
        else:
            mem_sec, mem = split_mem
        if fl_toggle_do:
            mult_acc.append(mem_sec)
        fl_toggle_do = not fl_toggle_do

    res = only_mults("".join(mult_acc))
    return res


def solve(lines: tuple[str, ...]):
    mem = "".join(lines)
    res = only_mults(mem)
    print(res)

    part_two_res = coded_mults(mem)
    print(part_two_res)


def main():
    lines = tuple(i for i in open("input.txt").readlines())
    solve(lines)


if __name__ == "__main__":
    main()
