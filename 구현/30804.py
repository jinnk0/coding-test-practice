import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())
fruits = list(map(int, input().split()))

left = 0
count = defaultdict(int)
max_len = 0

for right in range(N):
    count[fruits[right]] += 1

    while len(count) > 2:
        count[fruits[left]] -= 1
        if count[fruits[left]] == 0:
            del count[fruits[left]]
        left += 1
    
    max_len = max(max_len, right - left + 1)

print(max_len)