trees = [[]]
width = 0
height = 0
# [column][height]: depth
northVis = [[]]
southVis = [[]]
# [row][height]: depth
eastVis = [[]]
westVis = [[]]

if __name__ == "__main__":
    #file = open("input/treehouseSample.txt")
    file = open("input/treehouseSurvey.txt")
    lines = file.readlines()

    width = len(lines[0].strip())
    height = len(lines)
    trees = [[0] * width for i in range(height)]
    for y in range(height):
        line = lines[y]
        for x in range(width):
            trees[y][x] = int(line[x])
    
    # Evaluate visibility depths O(N^2)
    northVis = [[-1] * 10 for i in range(width)]
    southVis = [[-1] * 10 for i in range(width)]
    eastVis = [[-1] * 10 for i in range(height)]
    westVis = [[-1] * 10 for i in range(height)]
    # North + west
    for y in range(height):
        for x in range(width):
            tree = trees[y][x]
            for t in range(tree + 1):
                if northVis[x][t] == -1:
                    northVis[x][t] = y
            for t in range(tree + 1):
                if westVis[y][t] == -1:
                    westVis[y][t] = x
    
    # South + east
    for y in range(-1, -height-1, -1):
        for x in range(-1, -width-1, -1):
            tree = trees[y][x]
            for t in range(tree + 1):
                if southVis[x][t] == -1:
                    southVis[x][t] = y + height
            for t in range(tree + 1):
                if eastVis[y][t] == -1:
                    eastVis[y][t] = x + width

    # Evaluate tree visibility O(N^2)
    visibleTrees = 2 * width + 2 * height - 4
    for y in range(1, height-1):
        for x in range(1, width-1):
            tree = trees[y][x]
            if y > northVis[x][tree] and y < southVis[x][tree]:
                if x > westVis[y][tree] and x < eastVis[y][tree]:
                    continue
            visibleTrees += 1
    
    # Find best scenic score O(N^3)
    highestScenicScore = 0
    for y in range(1, height-1):
        for x in range(1, width-1):
            tree = trees[y][x]
            northScore = 0
            for y2 in range(y-1, -1, -1):
                northScore += 1
                if trees[y2][x] >= tree: break
            southScore = 0
            for y2 in range(y+1, height, 1):
                southScore += 1
                if trees[y2][x] >= tree: break
            eastScore = 0
            for x2 in range(x-1, -1, -1):
                eastScore += 1
                if trees[y][x2] >= tree: break
            westScore = 0
            for x2 in range(x+1, width, 1):
                westScore += 1
                if trees[y][x2] >= tree: break
            score = northScore * southScore * eastScore * westScore
            if score > highestScenicScore:
                highestScenicScore = score
    
    print(f"Boy howdy we can see a whopping {visibleTrees} trees in this here forest!")
    print(f"I'll tell the elves one of them there trees has a scenic score of {highestScenicScore} oowee!")