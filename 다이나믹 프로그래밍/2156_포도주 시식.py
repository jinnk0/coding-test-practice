'''
# 출처 : 백준 2156 포도주 시식 (실버1) 
# 유형 : 다이나믹 프로그래밍
# 포도주 잔 연속 3개 시식 불가능
# 최대로 마실 수 있는 포도주의 양 구하기
'''
# 이번 잔을 안 마시는 경우
# 이번 잔을 마시고, 이전 잔은 안 마신 경우
# 이번 잔을 마시고, 이전 잔도 마신 경우
import sys
input = sys.stdin.readline

n = int(input())
DP = [[0] * 3 for _ in range(n+1)]

for i in range(1, n+1):
    wine = int(input())
    if i > 1:
        DP[i][0] = max(DP[i-1])
        DP[i][1] = wine + max(DP[i-2])
        DP[i][2] = wine + max(DP[i-1][:2])
    else:
        DP[i][1] = wine
        DP[i][2] = wine

print(max(DP[n]))
