'''
# 출처 : 9095 1, 2, 3 더하기 (실버3)
# 유형 : 다이나믹 프로그래밍
'''
import sys
input = sys.stdin.readline

T = int(input())
cases = [int(input()) for _ in range(T)]

maximum = max(cases)
dp = [0] * max(4, (maximum + 1))
dp[1], dp[2], dp[3] = 1, 2, 4

for i in range(4, maximum + 1):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for case in cases:
    print(dp[case])