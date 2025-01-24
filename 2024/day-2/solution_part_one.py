import collections


def part_one(lines):
    count_safe = 0
    for report in lines:
        levels = list(map(int, report.split()))
        steps = []
        ind = 0
        end = len(levels) - 1
        # print(levels, ind, end)
        while ind < end:
            step = levels[ind]-levels[ind+1]
            steps.append(step)
            # print(step)
            ind += 1
        step_sequence_check = False

        if all([i < 0 for i in steps]) or all([i > 0 for i in steps]):
            step_sequence_check = True

        step_size_check = [bool(1 <= abs(s) <= 3) for s in steps]

        if all(step_size_check) and step_sequence_check:
            # print("safe")
            count_safe += 1
    print(count_safe)


def part_two(lines):
    count_safe = 0
    for report in lines:
        levels = list(map(int, report.split()))
        steps = []
        ind = 0
        end = len(levels) - 1
        # print(levels, ind, end)
        while ind < end:
            step = levels[ind]-levels[ind+1]
            steps.append(step)
            # print(step)
            ind += 1
        step_sequence_check = False

        pos_seq_group = [i < 0 for i in steps]
        neg_seq_group = [i > 0 for i in steps]

        if all(pos_seq_group) or all(neg_seq_group):
            step_sequence_check = True
        else:
            counter = collections.Counter(pos_seq_group)
            # print(counter)
            for k in counter:
                if counter[k] == 1:
                    idx = pos_seq_group.index(counter[k])
                    pos_seq_group.pop(idx)
                    neg_seq_group.pop(idx)
                    steps.pop(idx)
                    step_sequence_check = True

        step_size_check = [bool(1 <= abs(s) <= 3) for s in steps]

        if all(step_size_check) and step_sequence_check:
            # print("safe")
            count_safe += 1
    print(count_safe)


def main():
    lines = tuple(i for i in open("input.txt").readlines())
    part_one(lines)
    part_two(lines)


if __name__ == "__main__":
    main()
