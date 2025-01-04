n, m = map(int, input().split())
candy = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:  
            dp[i][j] = candy[i][j]
        elif i == 0:  
            dp[i][j] = dp[i][j-1] + candy[i][j]
        elif j == 0: 
            dp[i][j] = dp[i-1][j] + candy[i][j]
        else:
            dp[i][j] = candy[i][j] + max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

print(dp[n-1][m-1])