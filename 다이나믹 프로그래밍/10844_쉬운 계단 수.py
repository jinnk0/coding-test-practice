'''
# 출처 : 백준 10844 쉬운 계단 수 (실버1)
# 유형 : 다이나믹 프로그래밍
# 계단수 : 인접한 모든 자리수와의 차이가 1인 수
# 길이가 N인 계단수의 총 개수 구하기 (단, 0으로 시작하는 계단수는 없음)
'''
# 차이가 1인 수로 끝나는 N-1 길이의 계단수 개수 합산
N = int(input())
MOD = 1_000_000_000
DP = [[1]*10 for _ in range(N+1)]
DP[1][0] = 0

for i in range(2, N+1):
    for j in range(0, 10):
        if j > 0 and j < 9:
            DP[i][j] = (DP[i-1][j-1] + DP[i-1][j+1]) % MOD
        else:
            if j == 0:
                DP[i][j] = DP[i-1][j+1]
            else:
                DP[i][j] = DP[i-1][j-1]

print(sum(DP[N]) % MOD)
