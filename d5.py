import collections
import re

with open("d5input.txt") as f:
    data = f.read()
    lines = data.split('\n')

    stacks1 = [collections.deque() for i in range(9)]

    for l in lines[:8]:
        crates = re.findall('([A-Z]|\s{3})', l)
        for e, c in enumerate(crates):
            if c.strip():
                stacks1[e].append(c)

    stacks2 = [list(s) for s in stacks1]

    for l in lines[10:]:
        amount, from_, to = map(int, re.findall('\d+', l))

        for a in range(amount):
            stacks1[to - 1].appendleft(stacks1[from_ - 1].popleft())

        stacks2[to - 1] = stacks2[from_ - 1][:amount] + stacks2[to - 1]
        stacks2[from_ - 1] = stacks2[from_ - 1][amount:]

    answer1 = ''.join(s[0] for s in stacks1)
    answer2 = ''.join(s[0] for s in stacks2)

    print(answer1, answer2)

