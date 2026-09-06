import itertools as it

import aoc

houses = {(0, 0)}

xs = 0
ys = 0
xr = 0
yr = 0
for sr in it.batched(aoc.input(), 2):
    match sr[0]:
        case '>':
            xs += 1
        case '<':
            xs -= 1
        case '^':
            ys += 1
        case 'v':
            ys -= 1
    if len(sr) > 1:
        match sr[1]:
            case '>':
                xr += 1
            case '<':
                xr -= 1
            case '^':
                yr += 1
            case 'v':
                yr -= 1
    houses.add((xs, ys))
    houses.add((xr, yr))

print(len(houses))
