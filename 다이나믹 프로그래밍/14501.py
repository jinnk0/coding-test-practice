'''
# 출처 : 백준 14501 퇴사 (실버3)
# 유형 : 다이나믹 프로그래밍, 브루트포스
'''
import sys
input = sys.stdin.readline

N = int(input())
DP = [0] * (N+1)
for i in range(1, N+1):
    T, P = map(int, input().split())
    if i + T - 1 <= N:
        DP[i+T-1] = max(DP[i-1] + P, DP[i+T-1])
    DP[i] = max(DP[i-1], DP[i])
print(DP[N])