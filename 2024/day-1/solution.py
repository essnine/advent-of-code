def part_one(col1, col2):
    distances = []

    col1.sort()
    col2.sort()

    for i, val1 in enumerate(col1):
        distances.append(abs(int(val1) - int(col2[i])))
    print(sum(distances))


def part_two(col1, col2):
    sim_score = 0
    for val in col1:
        sim_score += int(val) * col2.count(val)
    print(sim_score)


def main():
    lines = tuple(i.split() for i in open("input.txt", "r").readlines() if len(i))
    col1 = []
    col2 = []

    for l1, l2 in lines:
        col1.append(l1)
        col2.append(l2)

    part_one(col1, col2)
    part_two(col1, col2)


if __name__ == "__main__":
    main()
