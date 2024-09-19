from collections import Counter

s1 = Counter(input())
s2 = Counter(input())

s1_s2 = s1 - s2
s2_s1 = s2 - s1

print(sum(s1_s2.values()) + sum(s2_s1.values()))
