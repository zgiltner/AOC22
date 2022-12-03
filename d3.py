with open("d3input.txt") as f:
    data = f.read().splitlines()
    pritotal = 0

# part 1 find total of priority
for line in data:
    half = len(line) // 2
    firsthalf = (line[:-half])
    secondhalf = (line[half:])
    itemtype = []
    #find intersection of first half and second half
    itemtype.extend(set(firsthalf).intersection(secondhalf))
    #make the set into a single letter
    letter = itemtype[0]
    #goofy ord() stuff
    if ord(letter) < 91:
        pritotal += (ord(letter)-38)
    else:
        pritotal += (ord(letter)-96)

#part 1 solution
print(pritotal)

# find intersection of every 3 lines
badgetotal = 0

for line in range(0, len(data), 3):
    firstline = data[line]
    secondline = data[line+1]
    thirdline = data[line+2]
    groupbadges = []
    groupbadges.extend(set(firstline).intersection(secondline, thirdline))
    badge = groupbadges[0]
    if ord(badge) < 91:
        badgetotal += (ord(badge)-38)
    else:
        badgetotal += (ord(badge)-96)

#part 2 solution
print(badgetotal)





