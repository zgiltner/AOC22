with open("d6input.txt") as f:
    data = f.read().strip()


def search(size):
    for i in range(len(data)-size):
        if len(set(data[i:i+size])) == size:
            return i+size


print(f"Part 1: {search(4)}")
print(f"Part 2: {search(14)}")
