originalSensorList = []
with open("input/d15input.txt", "r") as data:
    for t in data:
        Line = t.strip()
        _, _, sX, sY, _, _, _, _, bX, bY = Line.split()
        sX, sY, bX, bY = int(sX[2:-1]), int(sY[2:-1]), int(bX[2:-1]), int(bY[2:])
        newTuple = (sX, sY, bX, bY)
        originalSensorList.append(newTuple)


sensorList = []
beaconSet = set()
minY, minX = 10**10, 10**10
maxX, maxY = 0,0

for sX, sY, bX, bY in originalSensorList:
    beaconSet.add((bX,bY))
    radius = abs(sX-bX) + abs(sY-bY)
    newTuple = (sX, sY, radius)
    sensorList.append(newTuple)
    if sX-radius < minX:
        minX = sX-radius
    if sX+radius > maxX:
        maxX = sX+radius
    if sY-radius < minY:
        minY = sY-radius
    if sY+radius > maxY:
        maxY = sY+radius


def checkpointforinranges(pX, pY):
    inAnyRadius = False
    for sX, sY, radius in sensorList:
        if abs(sX - pX) + abs(sY - pY) <= radius:
            inAnyRadius = True
            break
    return inAnyRadius


def yieldcoordinates(sX, sY, radius):
    print("Activated")
    maxRange = 4000000
    for d in range(radius + 1):
        pX, pY = sX - radius + d - 1, sY + d
        if pX > maxRange or pX < 0 or pY > maxRange or pY < 0:
            continue
        yield pX, pY
    for d in range(radius + 1):
        pX, pY = sX + d, sY + radius - d + 1
        if pX > maxRange or pX < 0 or pY > maxRange or pY < 0:
            continue
        yield pX, pY
    for d in range(radius + 1):
        pX, pY = sX + radius - d + 1, sY - d
        if pX > maxRange or pX < 0 or pY > maxRange or pY < 0:
            continue
        yield pX, pY
    for d in range(radius + 1):
        pX, pY = sX - d, sY - radius + d - 1
        if pX > maxRange or pX < 0 or pY > maxRange or pY < 0:
            continue
        yield pX, pY
    yield -1, -1


for v, s in enumerate(sensorList):
    print(v)
    sX, sY, radius = s
    coordinateGenerator = yieldcoordinates(sX, sY, radius)
    coordinateFound = False
    for t in range(radius * 4):
        pX, pY = next(coordinateGenerator)
        if pX == -1 and pY == -1:
            break
        if not (checkpointforinranges(pX, pY)):
            coordinateFound = True
            fX, fY = pX, pY
            break
    if coordinateFound:
        break

part2answer = fX * 4000000 + fY
print(part2answer)
