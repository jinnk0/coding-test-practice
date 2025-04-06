'''
# 출처 : 백준 15990 1, 2, 3 더하기 5 (실버1)
# 유형 : 다이나믹 프로그래밍
# 각 수를 1, 2, 3만을 사용하여 덧셈으로 만들 때 만들 수 있는 경우의 수
# 단, 연속해서 같은 수 사용 불가
'''
# 1, 2, 3 으로 끝나는 경우를 고려하여 DP[i-1], DP[i-2], DP[i-3] 을 합산
# 단, 연속된 수는 더할 수 없으므로 DP[i-1], DP[i-2], DP[i-3]에서 각각 1, 2, 3으로 끝나는 경우 배제 
import sys
input = sys.stdin.readline
MOD = 1_000_000_009
MAX_INDEX = 100_000

DP = [[0] * 4 for _ in range(MAX_INDEX+1)]
DP[1][1] = 1
DP[2][2] = 1
DP[3][1] = 1
DP[3][2] = 1
DP[3][3] = 1
for i in range(4, MAX_INDEX+1):
        DP[i][1] = (DP[i-1][2] + DP[i-1][3]) % MOD
        DP[i][2] = (DP[i-2][1] + DP[i-2][3]) % MOD
        DP[i][3] = (DP[i-3][1] + DP[i-3][2]) % MOD

T = int(input())
for _ in range(T):
    n = int(input())
    print(sum(DP[n]) % MOD)