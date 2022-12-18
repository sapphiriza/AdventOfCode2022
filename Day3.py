def getprio(c):
    if(c.isupper()):
        return ord(c) - ord('A') + 27
    else:
        return ord(c) - ord('a') + 1

if __name__ == "__main__":
    lines = open("input/rucksacks.txt").readlines()

    prioritySum = 0
    for line in lines:
        line = line.strip()
        middle = int(len(line) / 2)
        left = line[:middle]
        right = line[middle:]
        for c in left:
            if c in right:
                prioritySum += getprio(c)
                break
    print("The sum of priorities for all errored items is " + str(prioritySum))

    badgeSum = 0
    for i in range(0, len(lines), 3):
        first = lines[i]
        second = lines[i+1]
        third = lines[i+2]
        for c in first:
            if c in second and c in third:
                badgeSum += getprio(c)
                break
    print("The sum of priorities for all badges is " + str(badgeSum))