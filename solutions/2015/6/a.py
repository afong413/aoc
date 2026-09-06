import aoc

lights = set()


def rect(x1, y1, x2, y2):
    return {(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)}


for inst in aoc.lines():
    inst = inst.split()
    match inst[0]:
        case 'toggle':
            x1, y1 = [int(x) for x in inst[1].split(',')]
            x2, y2 = [int(x) for x in inst[3].split(',')]
            lights.symmetric_difference_update(rect(x1, y1, x2, y2))
        case 'turn':
            x1, y1 = [int(x) for x in inst[2].split(',')]
            x2, y2 = [int(x) for x in inst[4].split(',')]
            match inst[1]:
                case 'on':
                    lights.update(rect(x1, y1, x2, y2))
                case 'off':
                    lights.difference_update(rect(x1, y1, x2, y2))

print(len(lights))
