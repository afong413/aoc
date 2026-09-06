import aoc

ans = 0

for word in aoc.lines():
    word += ' '
    xyx = False
    double = False
    for i in range(len(word) - 2):
        if word[i] == word[i + 2]:
            xyx = True
        for j in range(i + 2, len(word) - 2):
            if word[i : i + 2] == word[j : j + 2]:
                double = True
        if xyx and double:
            ans += 1
            break

print(ans)
