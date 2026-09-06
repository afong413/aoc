import numpy as np

import aoc

ribbon = 0

for box in aoc.lines():
    if not box.strip():
        continue
    dims = [int(d) for d in box.split('x')]
    ribbon += np.prod(dims) + 2 * (sum(dims) - max(dims))

print(ribbon)
