import aoc

ans = 0

for word in aoc.lines():
    word += ' '
    v = 0
    d = False
    for i in range(len(word) - 1):
        if word[i] in 'aeiou':
            v += 1
        if word[i] == word[i + 1]:
            d = True
        if word[i : i + 2] in ['ab', 'cd', 'pq', 'xy']:
            break
    else:
        if v >= 3 and d:
            ans += 1

print(ans)
