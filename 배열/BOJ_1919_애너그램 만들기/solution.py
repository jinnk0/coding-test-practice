s1 = input().strip()
s2 = input().strip()

alphabet_count = [0] * 26

for char in s1:
    alphabet_count[ord(char) - ord('a')] += 1
for char in s2:
    alphabet_count[ord(char) - ord('a')] -= 1

result = 0
for count in alphabet_count:
    result += abs(count)

print(result)