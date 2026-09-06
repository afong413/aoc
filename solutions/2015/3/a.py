import aoc

houses = {(0, 0)}

x = 0
y = 0
for c in aoc.input():
    match c:
        case '>':
            x += 1
        case '<':
            x -= 1
        case '^':
            y += 1
        case 'v':
            y -= 1
    houses.add((x, y))

print(len(houses))
