'''
# 출처 : 백준 2607 비슷한 단어
# 난이도 : 실버2
# 유형 : 구현, 문자열
'''
import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
default_word = input().strip()
words = [input().strip() for _ in range(N-1)]
count = 0

counter1 = Counter(default_word)
for word in words:
    counter2 = Counter(word)
    diff = sum((counter1 - counter2).values()) + sum((counter2 - counter1).values())
    if len(word) == len(default_word) and diff == 2:
        count += 1
    elif abs(len(word) - len(default_word)) == 1 and diff == 1:
        count += 1
    elif diff == 0:
        count += 1

print(count)