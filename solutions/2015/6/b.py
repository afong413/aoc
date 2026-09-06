from collections import defaultdict

import aoc

lights = defaultdict(int)


def rect(x1, y1, x2, y2):
    return ((x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1))


for inst in aoc.lines():
    inst = inst.split()
    match inst[0]:
        case 'toggle':
            x1, y1 = [int(x) for x in inst[1].split(',')]
            x2, y2 = [int(x) for x in inst[3].split(',')]
            for loc in rect(x1, y1, x2, y2):
                lights[loc] += 2
        case 'turn':
            x1, y1 = [int(x) for x in inst[2].split(',')]
            x2, y2 = [int(x) for x in inst[4].split(',')]
            match inst[1]:
                case 'on':
                    for loc in rect(x1, y1, x2, y2):
                        lights[loc] += 1
                case 'off':
                    for loc in rect(x1, y1, x2, y2):
                        lights[loc] = max(0, lights[loc] - 1)

print(sum(lights.values()))
