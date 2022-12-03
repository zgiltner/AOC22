with open("d3input.txt") as f:
    data = f.read().splitlines()
    priTotal = 0

# part 1 find total of priority
for line in data:
    half = len(line) // 2
    firstHalf = (line[:-half])
    secondHalf = (line[half:])
    itemType = []
# find intersection of first half and second half
    itemType.extend(set(firstHalf).intersection(secondHalf))
# make the set into a single letter
    letter = itemType[0]
# goofy ord() stuff
    if ord(letter) < 91:
        priTotal += (ord(letter)-38)
    else:
        priTotal += (ord(letter)-96)

# part 1 solution
print(priTotal)

# find intersection of every 3 lines
badgeTotal = 0

for line in range(0, len(data), 3):
    firstLine = data[line]
    secondLine = data[line+1]
    thirdLine = data[line+2]
    groupBadges = []
    groupBadges.extend(set(firstLine).intersection(secondLine, thirdLine))
    badge = groupBadges[0]
    if ord(badge) < 91:
        badgeTotal += (ord(badge)-38)
    else:
        badgeTotal += (ord(badge)-96)

# part 2 solution
print(badgeTotal)
