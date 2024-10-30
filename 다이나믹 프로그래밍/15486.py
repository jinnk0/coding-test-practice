import sys

input = sys.stdin.readline
N = int(input())
DP = [0] * (N + 1)

for i in range(N):
    t, p = map(int, input().split())
    DP[i+1] = max(DP[i+1], DP[i])
    if t + i <= N:
        DP[t + i] = max(DP[t + i], DP[i] + p)

print(max(DP))