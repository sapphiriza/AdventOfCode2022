def draw():
    global cycle
    global x
    p = (cycle - 1) % 40
    print('#' if abs(p - x) <= 1 else '.', end='' if p != 39 else '\n')

def doCycle():
    global cycle
    global signalSum
    cycle += 1
    draw()

    if (cycle - 20) % 40 == 0:
        signalSum += x * cycle
        #print(f"Signal strength at cycle {cycle} is {x * cycle}, with x={x}")

if __name__ == "__main__":
    #file = open("input/signalSample.txt")
    file = open("input/signalOps.txt")
    lines = file.readlines()

    global x
    x = 1
    cycle = 1
    signalSum = 0
    for line in lines:
        if line.startswith("addx"):
            doCycle()
            add = line.strip()[4:]
            add = int(add)
            x += add
        doCycle()

    print(f"Sum signal strength is {signalSum}")

