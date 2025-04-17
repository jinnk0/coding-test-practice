'''
# 출처 : 백준 1149 RGB거리 (실버1)
# 유형 : 다이나믹 프로그래밍
# 1 ~ N까지의 집을 빨강, 초록, 파랑 중 하나의 색으로 칠함
# 인접한 집의 색은 달라야 함
# 모든 집을 칠하는 비용의 최소값 구하기
'''
# 각 집을 빨강, 초록, 파랑으로 칠할 때의 경우의 수를 나누어 계산
# 각 경우의 수 별로 이전 집의 색에 따른 최소 비용 계산
import sys
input = sys.stdin.readline

N = int(input())
DP = [list(map(int, input().strip().split())) for _ in range(N)]

for i in range(1, N):
    DP[i][0] = min(DP[i][0] + DP[i-1][1], DP[i][0] + DP[i-1][2])
    DP[i][1] = min(DP[i][1] + DP[i-1][0], DP[i][1] + DP[i-1][2])
    DP[i][2] = min(DP[i][2] + DP[i-1][0], DP[i][2] + DP[i-1][1])

print(min(DP[N-1]))