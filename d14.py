rocks = [list(map(eval, s.strip().split(' -> '))) for s in open("input/d14input.txt").read().splitlines()]
maxY = max([xy[1] for ridge in rocks for xy in ridge])
maxX = max([xy[0] for ridge in rocks for xy in ridge])


def paintRidges():
    for ridge in rocks:
        for i in range(len(ridge) - 1):
            x1, y1, x2, y2 = ridge[i][0], ridge[i][1], ridge[i + 1][0], ridge[i + 1][1]
            for y in range(min(y1, y2), max(y1, y2) + 1):
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    grid[y][x] = '#'


def dropGrain():
    (x, y) = (500, 0)
    while (y < maxY):
        y += 1
        if grid[y][x] == '.':
            pass
        elif grid[y][x - 1] == '.':
            x -= 1
        elif grid[y][x + 1] == '.':
            x += 1
        else:
            grid[y - 1][x] = 'o'
            return True
    return False

grid = [['.'] * (maxX + 2) for _ in range(maxY + 1)]
paintRidges()
grains = 0
while dropGrain():
    grains += 1

print(grains)


maxY += 2
grid = [['.'] * (501 + maxY) for _ in range(maxY)]
grid += [['#'] * (501 + maxY)]  # a large enough floor
paintRidges()
grains = 0
while grid[0][500] == '.':
    dropGrain()
    grains += 1

print(grains)



