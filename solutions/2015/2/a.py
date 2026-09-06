import itertools as it

import aoc

paper = 0

for box in aoc.lines():
    dims = [int(d) for d in box.split('x')]
    sides = [a * b for a, b in it.combinations(dims, 2)]
    paper += 2 * sum(sides) + min(sides)

print(paper)
