import aoc

floor = 0

for c in aoc.input():
    match c:
        case '(':
            floor += 1
        case ')':
            floor -= 1

print(floor)
