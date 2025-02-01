import os
import sys
import timeit
from math import floor

def check_correctness(rule_set: set, pageset) -> tuple[bool, tuple[int, int] | None]:
    ptr = 0
    max = len(pageset)-1
    valid = True
    while ptr < (max) :
        for i in range(ptr, max):
            page_combo = "|".join((pageset[ptr], pageset[i+1],))
            rev_page_combo = "|".join((pageset[i+1], pageset[ptr],))
            if page_combo not in rule_set or rev_page_combo in rule_set:
                valid = False
                break
        if not valid:
            break
        ptr += 1
    return valid, (ptr, i+1)


def solve(lines: tuple[str, ...]):
    bool_rules = True
    rule_set = set()
    pageset_list = []
    for line in lines:
        if bool_rules:
            if line.strip():
                rule_set.add(line)
            else:
                bool_rules = False
        else:
            pageset_list.append(line.split(","))
    
    correct_pageset_list = []
    incorrect_pageset_dict = {}
    for pageset in pageset_list:
        fl_valid, idxs = check_correctness(rule_set, pageset)
        if not fl_valid:
            pageset_tup = tuple(i for i in pageset)
            incorrect_pageset_dict[pageset_tup] = idxs
        else:
            correct_pageset_list.append(pageset)
    corr_acc = 0
    incorr_acc = 0
    for pageset in correct_pageset_list:
        mid = pageset[floor(len(pageset)/2)]
        corr_acc += int(mid)
    for pageset_tup in incorrect_pageset_dict:
        valid = False
        idxs = incorrect_pageset_dict[pageset_tup]
        _, idy = idxs
        pageset = list(pageset_tup)
        while (not valid):
            if idy == len(pageset):
                break
            idx, idy = idxs
            pageset[idx], pageset[idy] = pageset[idy], pageset[idx]
            valid, idxs = check_correctness(rule_set, pageset)
            # if valid:
                # print("corrected!")
        mid = pageset[floor(len(pageset)/2)]
        incorr_acc += int(mid)
    print("corr_acc: ", corr_acc)
    print("incorr_acc: ", incorr_acc)
    return


def main(input_filename="input.txt"):
    lines = tuple(i.strip() for i in open(input_filename).readlines() if len(i))
    solve(lines)


if __name__ == "__main__":
    path = os.path.dirname(__file__)
    input_filename = f"{path}/input.txt"
    if len(sys.argv) > 1:
        if sys.argv[1] == "test":
            input_filename = f"{path}/sample_input.txt"
    # main(input_filename)
    time_code_exec = timeit.timeit(main, number=1)
    print("ran main in {}".format(time_code_exec))
