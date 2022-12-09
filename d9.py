import numpy as np

with open("d9input.txt") as f:
    moves = f.read().split("\n")

# defining movement pattern and starting position and creating win condition
movement = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
headX, headY = 0, 0
tailX, tailY = 0, 0
visited = set()

# massaging the moves into a list of tuples
for line in moves:
    direction, steps = line.split()
    steps = int(steps)

    # moving the "rope"
    for _ in range(steps):
        headX, headY = headX + movement[direction][0], headY + movement[direction][1]
        distX, distY = headX - tailX, headY - tailY

        # does rope touch itself?
        if (abs(distX) >= 2) or (abs(distY) >= 2):
            tailX, tailY = tailX + np.sign(distX), tailY + np.sign(distY)

        visited |= {(tailX, tailY)}
# part 1 answer
print(len(visited))

# part 2
# starting position (again)
headX, headY = 0, 0
tailX, tailY = 0, 0
# ten knot rope
rope = [(0, 0)] * 10
# visited2 set
visited2 = set()

# massaging the moves into a list of tuples (again)
for line in moves:
    direction, steps = line.split()
    steps = int(steps)
    # moving the "rope"
    for _ in range(steps):
        headX, headY = rope[0]
        rope[0] = headX + movement[direction][0], headY + movement[direction][1]

        for i in range(len(rope) - 1):
            headX, headY = rope[i]
            tailX, tailY = rope[i + 1]
            distX, distY = headX - tailX, headY - tailY

            if (abs(distX) >= 2) or (abs(distY) >= 2):
                rope[i + 1] = tailX + np.sign(distX), tailY + np.sign(distY)

        visited2 |= {rope[-1]}
#part 2 answer
print(len(visited2))
















