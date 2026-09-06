from hashlib import md5

import aoc

key = aoc.input().strip()

n = 1
while True:
    if md5(f'{key}{n}'.encode()).hexdigest().startswith('00000'):
        print(n)
        break
    n += 1
