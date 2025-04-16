'''
# 출처 : 백준 15988 1, 2, 3 더하기 3 (실버2)
# 유형 : 다이나믹 프로그래밍
'''
import sys
input = sys.stdin.readline
MOD = 1_000_000_009
DP = [0] * 1000001
DP[1], DP[2], DP[3] = 1, 2, 4
for i in range(4, 1000001):
    DP[i] = (DP[i-1] + DP[i-2] + DP[i-3]) % MOD

T = int(input())
for _ in range(T):
    print(DP[int(input())])
