class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def add(self, pos):
        self.x += pos.x
        self.y += pos.y
    
    def isclose(self, pos):
        return abs(self.x - pos.x) <= 1 and abs(self.y - pos.y) <= 1
    
    def moveclose(self, pos):
        if notequal(self.x, pos.x):
            if self.x < pos.x:
                self.x += 1
            else:
                self.x -= 1
        if notequal(self.y, pos.y):
            if self.y < pos.y:
                self.y += 1
            else:
                self.y -= 1
    
    def tostr(self):
        return f"({self.x},{self.y})"
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

def print_visited(visited):
    minp = Position(0,0)
    maxp = Position(0,0)
    for v in visited:
        minp.x = min(minp.x, v.x)
        minp.y = min(minp.y, v.y)
        maxp.x = max(maxp.x, v.x)
        maxp.y = max(maxp.y, v.y)
    
    for y in range(maxp.y, minp.y-1 , -1):
        for x in range(minp.x, maxp.x+1):
            if Position(x,y) in visited:
                print('#', end='')
            else:
                print('.', end='')
        print()
                

def notequal(a, b):
    d = a - b
    return d > 0.0001 or d < -0.0001

if __name__ == "__main__":
    #file = open("input/ropeSample.txt")
    #file = open("input/ropeSample2.txt")
    file = open("input/ropeSway.txt")

    head = Position(0,0)
    tail = Position(0,0)
    visited = {Position(0,0)}

    knots = [Position(0,0) for _ in range(10)]
    visited2 = {Position(0,0)}

    for line in file.readlines():
        n = int(line[2:].strip())
        v = Position(0,0)

        if line[0] == 'L':
            v.x = -1
        elif line[0] == 'R':
            v.x = 1
        elif line[0] == 'U':
            v.y = 1
        else:
            v.y = -1
        
        for i in range(n):
            head.add(v)
            if not tail.isclose(head):
                tail.moveclose(head)
                visited.add(Position(tail.x, tail.y))
            knots[0].add(v)
            for i in range(1,len(knots)):
                if not knots[i].isclose(knots[i-1]):
                    knots[i].moveclose(knots[i-1])
            visited2.add(Position(knots[-1].x, knots[-1].y))
    
    #print_visited(visited2)

    print(f"That tail swung around to {len(visited2)} total positions!")