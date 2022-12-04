with open("d4input.txt") as f:
    data = f.read().splitlines()
    print(data)

coveredPairs = 0
# part 1
for line in data:
# get comparison ranges
    ranges = [[int(a), int(b)] for a, b in [x.split("-") for x in line.split(",")]]
# prepare sets to be compared and counted
    set_a = set(range(ranges[0][0], ranges[0][1] + 1))
    set_b = set(range(ranges[1][0], ranges[1][1] + 1))
# check if one set is a subset of the other
    if set_a.issubset(set_b) or set_b.issubset(set_a):
        coveredPairs += 1
# part 1 solution
print(coveredPairs)

# part 2
overlappingRanges = 0
for line in data:
    ranges = [[int(a), int(b)] for a, b in [x.split("-") for x in line.split(",")]]
    set_a = set(range(ranges[0][0], ranges[0][1] + 1))
    set_b = set(range(ranges[1][0], ranges[1][1] + 1))
    if set_a.intersection(set_b):
        overlappingRanges += 1
# part 2 solution
print(overlappingRanges)



