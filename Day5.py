import re

stacks = []
stacks2 = []

# Parse a line, inserting crates to the bottom of the columns
stackprog = re.compile(r"\[[A-Z]\]")
def parse(line):
    for i in stackprog.finditer(line):
        c = int(i.start() / 4)
        t = line[i.start() + 1]
        while len(stacks) <= c:
            stacks.append([])
        stacks[c].insert(0, t)

# Parse a line, moving crates from one column to the next
moveprog = re.compile(r"\d+")
def run(line):
    move = moveprog.findall(line)
    n = int(move[0])
    c0 = int(move[1]) - 1
    c1 = int(move[2]) - 1

    stacks[c1] += stacks[c0][:-n-1:-1]
    stacks2[c1] += stacks2[c0][-n:]
    stacks[c0][-n:] = []
    stacks2[c0][-n:] = []

#-=-========================================================================-=-#
if __name__ == "__main__":
    file = open("input/crateShuffle.txt")

    # Read in crates
    for line in file:
        if not line.strip():
            break
        parse(line)
    
    # Copy the stacks for the correct solution
    for stack in stacks:
        stacks2.append(stack.copy())
    
    # Move stacks around
    for line in file:
        run(line)
    
    result = ""
    result2 = ""
    for stack in stacks:
        #print(stack)
        result += stack[-1]
    for stack in stacks2:
        #print(stack)
        result2 += stack[-1]
    
    print(f"Aaand the top crates are: {result}")
    print(f"...hah nope! Chuck Testa: {result2}")
    