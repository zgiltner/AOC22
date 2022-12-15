import re

sensorX = []
sensorY = []
beaconX = []
beaconY = []
manhattanDistances = []
relevantSensorX = []
relevantSensorY = []
relevantManhattanDistances = []
xRange = []
sorting = []

with open("input/d15input.txt") as f:
    data = f.read().split("\n")

    for line in data:
        splitLine = line.split()
        sX = str(splitLine[2])
        cleanedsX = re.sub(r"(=)|(x)|(,)", "", sX)
        sensorX.append(cleanedsX)
        sY = str(splitLine[3])
        cleanedsY = re.sub(r"(=)|(y)|(:)|(,)", "", sY)
        sensorY.append(cleanedsY)
        bX = str(splitLine[8])
        cleanedbX = re.sub(r"(=)|(x)|(,)", "", bX)
        beaconX.append(cleanedbX)
        bY = str(splitLine[9])
        cleanedbY = re.sub(r"(=)|(y)|(,)", "", bY)
        beaconY.append(cleanedbY)

# find the manhattan distance between each sensor and beacon
for i in range(len(sensorX)):
    manhattanDistances.append(abs(int(sensorX[i]) - int(beaconX[i])) + abs(int(sensorY[i]) - int(beaconY[i])))

# find relevant sensors
for i in range(len(sensorX)):
    if (int(sensorY[i]) - manhattanDistances[i]) < 10 < (int(sensorY[i]) + manhattanDistances[i]):
        relevantSensorX.append(sensorX[i])
        relevantSensorY.append(sensorY[i])
        relevantManhattanDistances.append(manhattanDistances[i])

# find x values for y = 10 or 10
for i in range(len(relevantSensorX)):
    yDiff = abs(10 - int(relevantSensorY[i]))
    expand = relevantManhattanDistances[i] - yDiff
    lowX = int(relevantSensorX[i]) - expand
    highX = int(relevantSensorX[i]) + expand
    xRange.append([lowX, highX])

# print(xRange)
for begin, end in sorted(xRange):
    if sorting and sorting[-1][1] >= begin - 1:
        sorting[-1][1] = max(sorting[-1][1], end)
    else:
        sorting.append([begin, end])

print(sorting)
part1answer = sorting[0][1] - sorting[0][0]
print(part1answer)
