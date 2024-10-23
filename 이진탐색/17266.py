import sys

input = sys.stdin.readline
N = int(input())
M = int(input())
X = list(map(int, input().split()))

def light(height):
    start = 0
    for x in X:
        if x - height <= start:
            start = x + height
        else:
            return False
    return start >= N

start, end = 1, N
while start <= end:
    mid = (start + end) // 2
    if light(mid):
        end = mid - 1
    else:
        start = mid + 1

print(start)