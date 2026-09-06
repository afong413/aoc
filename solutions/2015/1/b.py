import aoc

floor = 0

for i, c in enumerate(aoc.input()):
    match c:
        case '(':
            floor += 1
        case ')':
            floor -= 1
    if floor < 0:
        print(i + 1)
        break
