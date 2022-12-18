if __name__ == "__main__":
    file = open("input/rpsStrategy.txt")
    wrongScore = 0
    rightScore = 0
    for line in file.readlines():
        o = ord(line[0]) - ord('A')
        r = ord(line[2]) - ord('X')

        diff = (r - o + 1) % 3
        wrongScore += (r + 1) + (diff * 3)

        s = (o + (r - 1)) % 3
        rightScore += (s + 1) + (r * 3)
    print("The wrong cheat guide would give you a score of " + str(wrongScore))
    print("The 'correct' cheat guide would give you a score of " + str(rightScore))
