import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[[float('inf')] * 3 for _ in range(M)] for _ in range(N)]

for j in range(M):
    for k in range(3):
        dp[0][j][k] = grid[0][j]

for i in range(1, N):
    for j in range(M):
        for k in range(3):
            if k != 0 and j > 0:
                dp[i][j][0] = min(dp[i][j][0], dp[i-1][j-1][1], dp[i-1][j-1][2]) + grid[i][j]
            if k != 1:
                dp[i][j][1] = min(dp[i][j][1], dp[i-1][j][0], dp[i-1][j][2]) + grid[i][j]
            if k != 2 and j < M-1:
                dp[i][j][2] = min(dp[i][j][2], dp[i-1][j+1][0], dp[i-1][j+1][1]) + grid[i][j]

result = float('inf')
for j in range(M):
    result = min(result, dp[N-1][j][0], dp[N-1][j][1], dp[N-1][j][2])

print(result)
