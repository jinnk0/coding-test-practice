import sys

input = sys.stdin.readline
N, M = map(int, input().split())
moneys = [int(input()) for _ in range(N)]

DP = [-1] * (M + 1)
DP[0] = 0
for i in range(N):
    for j in range(moneys[i], M + 1):
        if DP[j - moneys[i]] != -1:
            if DP[j] >= 0:
                DP[j] = min(DP[j], DP[j - moneys[i]] + 1)
            else:
                DP[j] = DP[j - moneys[i]] + 1

print(DP[M])