with open("d10input.txt") as f:
    instructions = f.read().split("\n")
x, cycle = 1, 1
twenty, sixty, hundred, oneForty, oneEighty, twoTwenty = 0, 0, 0, 0, 0, 0
oneToForty, fortyOneToEighty, eightyOneToOneTwenty, OneTwentyOneToOneSixty, oneSixtyOneToTwoHundred, twoHundredOneToTwoHundredForty = [], [], [], [], [], []


def tube():
    if cycle < 41:
        index = cycle - 1
        pixel = [x - 1, x, x + 1]
        if index in pixel:
            oneToForty.insert(index, "#")
        else:
            oneToForty.insert(index, ".")
    elif cycle < 81:
        index = cycle - 41
        pixel = [x - 1, x, x + 1]
        if index in pixel:
            fortyOneToEighty.insert(index, "#")
        else:
            fortyOneToEighty.insert(index, ".")
    elif cycle < 121:
        index = cycle - 81
        pixel = [x - 1, x, x + 1]
        if index in pixel:
            eightyOneToOneTwenty.insert(index, "#")
        else:
            eightyOneToOneTwenty.insert(index, ".")
    elif cycle < 161:
        index = cycle - 121
        pixel = [x - 1, x, x + 1]
        if index in pixel:
            OneTwentyOneToOneSixty.insert(index, "#")
        else:
            OneTwentyOneToOneSixty.insert(index, ".")
    elif cycle < 201:
        index = cycle - 161
        pixel = [x - 1, x, x + 1]
        if index in pixel:
            oneSixtyOneToTwoHundred.insert(index, "#")
        else:
            oneSixtyOneToTwoHundred.insert(index, ".")
    elif cycle < 241:
        index = cycle - 201
        pixel = [x - 1, x, x + 1]
        if index in pixel:
            twoHundredOneToTwoHundredForty.insert(index, "#")
        else:
            twoHundredOneToTwoHundredForty.insert(index, ".")


def signal():
    global twenty, sixty, hundred, oneForty, oneEighty, twoTwenty
    if cycle == 20:
        twenty = cycle * x
    elif cycle == 60:
        sixty = cycle * x
    elif cycle == 100:
        hundred = cycle * x
    elif cycle == 140:
        oneForty = cycle * x
    elif cycle == 180:
        oneEighty = cycle * x
    elif cycle == 220:
        twoTwenty = cycle * x


for line in instructions:
    if line == "noop":
        tube()
        cycle += 1

    else:
        tube()
        signal()
        cycle += 1
        tube()
        signal()
        cycle += 1
        xvalue = int(line.split()[1])
        x += xvalue

# part 1 answer
print(sum([twenty, sixty, hundred, oneForty, oneEighty, twoTwenty]))

# part 2
print(oneToForty)
print(fortyOneToEighty)
print(eightyOneToOneTwenty)
print(OneTwentyOneToOneSixty)
print(oneSixtyOneToTwoHundred)
print(twoHundredOneToTwoHundredForty)
