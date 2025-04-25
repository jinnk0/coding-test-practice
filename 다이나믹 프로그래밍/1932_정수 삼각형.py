'''
# 출처 : 백준 1932 정수 삼각형 (실버1)
# 유형 : 다이나믹 프로그래밍
# 각 줄이 1 ~ n인 크기가 n인 정수 삼각형
# 맨 위층(1)부터 아래에 있는 수 하나를 선택하여 아래층으로 내려올 때 선택한 수의 최대값
# 단, 아래층 수는 대각선에 있는 수만 선택 가능
'''
# 아래에서 위로, 아래층에서 선택할 수 있는 가장 큰 수와 합산하며 올라감 
import sys
input = sys.stdin.readline

n = int(input())
DP = [list(map(int, input().strip().split())) for _ in range(n)]

for i in range(n-2, -1, -1):
    for j in range(len(DP[i])):
        DP[i][j] = DP[i][j] + max(DP[i+1][j], DP[i+1][j+1])

print(DP[0][0])