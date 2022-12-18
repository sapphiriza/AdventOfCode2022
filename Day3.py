if __name__ == "__main__":
    file = open("input/rucksacks.txt")
    prioritySum = 0
    for line in file.readlines():
        line = line.strip()
        middle = int(len(line) / 2)
        left = line[:middle]
        right = line[middle:]
        for c in left:
            if c in right:
                priority = ord(c) - ord('A') + 27 if c.isupper() else ord(c) - ord('a') + 1
                prioritySum += priority
                break
    print("The sum of priorities for all errored items is " + str(prioritySum))