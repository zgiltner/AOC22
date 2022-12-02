with open("d2input.txt") as f:
    data = f.read().splitlines()
    print(data)

    totalscore = 0
    for line in data:
        if line == "A Y":
            totalscore += 8
        elif line == "A X":
            totalscore += 4
        elif line == "A Z":
            totalscore += 3
        elif line == "B Y":
            totalscore += 5
        elif line == "B X":
            totalscore += 1
        elif line == "B Z":
            totalscore += 9
        elif line == "C Y":
            totalscore += 2
        elif line == "C X":
            totalscore += 7
        elif line == "C Z":
            totalscore += 6
        else:
            totalscore += 0

    print(totalscore)

    parttwoscore = 0
    for line in data:
        if line == "A Y":
            parttwoscore += 4
        elif line == "A X":
            parttwoscore += 3
        elif line == "A Z":
            parttwoscore += 8
        elif line == "B Y":
            parttwoscore += 5
        elif line == "B X":
            parttwoscore += 1
        elif line == "B Z":
            parttwoscore += 9
        elif line == "C Y":
            parttwoscore += 6
        elif line == "C X":
            parttwoscore += 2
        elif line == "C Z":
            parttwoscore += 7
        else:
            parttwoscore += 0

    print(parttwoscore)

