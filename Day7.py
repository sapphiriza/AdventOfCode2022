dirTree = {"/":[]}
dirSizeCache = {}

# This is jacked. I don't give a shit it's 2AM
def stackToStr(stack):
    if len(stack) == 0:
        return ""
    result = ""
    for dir in stack:
        result += dir if result == "" else "/" + dir
    return result

def dirsum(topdir):
    #print(f"dirsum called on {topdir}: {dirTree[topdir]}")
    sum = dirSizeCache.get(topdir, 0)
    if sum > 0:
        return sum
    for item in dirTree[topdir]:
        if isinstance(item, int):
            sum += item
        elif isinstance(item, str):
            sum += dirsum(item)
    dirSizeCache[topdir] = sum
    return sum

if __name__ == "__main__":
    #file = open("input/dirSample.txt")
    file = open("input/dirSizes.txt")
    
    dirStack = ['/']
    directories = ['/']
    dirName = '/'
    for line in file:
        if line.startswith("$"):
            if line.startswith("$ cd"):
                dir = line[5:].strip()
                if dir == '/':
                    dirStack = ['/']
                elif dir == "..":
                    dirStack.pop()
                else:
                    dirStack.append(dir)
                dirName = stackToStr(dirStack)
        elif line.startswith("dir"):
            dir = line[4:].strip()
            dir = stackToStr(dirStack) + "/" + dir
            if dirTree[dirName].count(dir) == 0:
                dirTree[dirName].append(dir)
            
            if directories.count(dir) == 0:
                dirTree[dir] = []
                directories.append(dir)
        else:
            size = int(line.split()[0])
            dirTree[dirName].append(size)
    
    sum = 0
    for dir in directories:
        size = dirsum(dir)
        if size <= 100000:
            sum += size
    print(f"The sum of numbers below 100000 is {sum} in total! Good luck using that =D")

    spaceRequired = dirsum("/") - 40000000
    smallestDir = "/"
    smallestSize = dirsum("/")
    for dir in directories:
        size = dirsum(dir)
        if size > spaceRequired and size < smallestSize:
            smallestDir = dir
            smallestSize = size
    print(f"`rm {smallestDir}` would free up {dirsum(smallestDir)} disk space!")
