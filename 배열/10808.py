S = input()
count = [0] * 26
for s in S:
    count[ord(s)-97] += 1
print(' '.join(list(map(str, count))))