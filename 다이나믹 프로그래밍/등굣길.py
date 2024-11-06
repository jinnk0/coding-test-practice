def solution(m, n, puddles):
    DP = [[0] * (m+1) for _ in range(n+1)]
    DP[1][1] = 1
    for i in range(1, m+1):
        for j in range(1, n+1):
            if [i, j] in puddles:
                continue
            if i-1 > 0 and i-1 <= m:
                DP[j][i] += DP[j][i-1]
            if j-1 > 0 and j-1 <= n:
                DP[j][i] += DP[j-1][i]
    return DP[n][m] % 1000000007
