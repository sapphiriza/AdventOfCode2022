from queue import PriorityQueue

POS_NONE = (-1,-1)

class GridNode:
    def __init__(self):
        self.visited = False
        self.parent = POS_NONE
        self.height = 0
        self.pathlen = 0



def getHeuristic(x, y):
    h0 = gridmap[y][x].height
    h1 = gridmap[end[1]][end[0]].height
    return max(abs(x - end[0]) + abs(y - end[1]), max(h1 - h0, 0))

def tryVisiting(x, y, prev):
    if x < 0 or x >= width:
        return
    if y < 0 or y >= height:
        return
    if gridmap[y][x].visited:
        return
    
    h0 = gridmap[prev[1]][prev[0]].height
    h1 = gridmap[y][x].height
    if h1 > h0 + 1:
        return
    
    pathlen = gridmap[prev[1]][prev[0]].pathlen + 1
    heuristic = getHeuristic(x, y)
    openlist.put((pathlen + heuristic, (prev, (x, y))))

def tryVisiting2(x, y, prev):
    if x < 0 or x >= width:
        return
    if y < 0 or y >= height:
        return
    if gridmap[y][x].visited:
        return
    
    h0 = gridmap[prev[1]][prev[0]].height
    h1 = gridmap[y][x].height
    if h1 < h0 - 1:
        return
    
    pathlen = gridmap[prev[1]][prev[0]].pathlen + 1
    openlist.put((pathlen, (prev, (x, y))))

if __name__ == "__main__":
    #file = open("input/heightmapSample.txt")
    file = open("input/heightmap.txt")
    lines = file.readlines()

    width = 0
    for line in lines:
        w = len(line.strip())
        if w > width:
            width = w
    height = len(lines)
    
    start = (0,0)
    end = (width-1,height-1)
    gridmap = [[GridNode() for x in range(width)] for y in range(height)]
    for y in range(height):
        for x in range(width):
            c = lines[y][x]
            if not c.isupper():
                gridmap[y][x].height = ord(c) - ord('a')
            elif c == 'S':
                start = (x,y)
                gridmap[y][x].height = 0
            elif c == 'E':
                end = (x,y)
                gridmap[y][x].height = ord('z') - ord('a')

    print(f"W={width},H={height}")

    for y in range(height):
        for x in range(width):
            print(chr(ord('a') + gridmap[y][x].height),end='')
        print()
    
    openlist = PriorityQueue()
    openlist.put((getHeuristic(start[0], start[1]), (POS_NONE, start)))
    while not openlist.empty():
        visit = openlist.get()
        pos0 = visit[1][0]
        pos1 = visit[1][1]
        if gridmap[pos1[1]][pos1[0]].visited:
            continue
        
        gridmap[pos1[1]][pos1[0]].visited = True
        gridmap[pos1[1]][pos1[0]].parent = pos0
        pathlen = visit[0] - getHeuristic(pos1[0], pos1[1])
        gridmap[pos1[1]][pos1[0]].pathlen = pathlen

        if pos1 == end:
            break
        
        tryVisiting(pos1[0] + 1, pos1[1], pos1)
        tryVisiting(pos1[0] - 1, pos1[1], pos1)
        tryVisiting(pos1[0], pos1[1] + 1, pos1)
        tryVisiting(pos1[0], pos1[1] - 1, pos1)
    
    if gridmap[end[1]][end[0]].visited:
        print(f"Path found! It took {pathlen} steps to get there!")
    else:
        print("Path not found!")
    
    #Go backwards from the top till we find a valid one, using tryVisiting2 instead, which reverses the height check and ignores heuristic (breadth-first babyeee!!)
    for y in range(height):
        for x in range(width):
            gridmap[y][x].visited = False
    openlist = PriorityQueue()
    openlist.put((0, (POS_NONE, end)))
    trailFound = False
    while not openlist.empty():
        visit = openlist.get()
        pos0 = visit[1][0]
        pos1 = visit[1][1]
        if gridmap[pos1[1]][pos1[0]].visited:
            continue

        gridmap[pos1[1]][pos1[0]].visited = True
        gridmap[pos1[1]][pos1[0]].parent = pos0
        pathlen = visit[0]
        gridmap[pos1[1]][pos1[0]].pathlen = pathlen

        if gridmap[pos1[1]][pos1[0]].height == 0:
            trailFound = True
            break
        
        tryVisiting2(pos1[0] + 1, pos1[1], pos1)
        tryVisiting2(pos1[0] - 1, pos1[1], pos1)
        tryVisiting2(pos1[0], pos1[1] + 1, pos1)
        tryVisiting2(pos1[0], pos1[1] - 1, pos1)
    
    if trailFound:
        print(f"We got a good trail too! It's {pathlen} steps long!")
    else:
        print("No trail found either! wtf!!")