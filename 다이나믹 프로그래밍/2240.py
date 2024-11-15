'''
# 출처 : 백준
# 문제 유형 : 다이나믹 프로그래밍
# 입력
    - T : 자두가 떨어지는 총 시간(초) (1 <= T <= 1,000)
    - W : 자두가 떨어지는 자두를 받기 위해 움직이는 최대 횟수 (1 <= W <= 30)
    - 자두가 떨어지는 나무의 번호 총 T개(줄) (1 or 2)
# 출력 : 자두가 받을 수 있는 자두의 최대 개수
'''
import sys

input = sys.stdin.readline
T, W = map(int, input().split())
plums = [int(input()) for _ in range(T)]

DP = [[0] * (W+1) for _ in range(T+1)]

for t in range(1, T+1):
    for w in range(W+1):
        if w > 0:
            if w % 2 + 1 == plums[t-1]:
                DP[t][w] = max(DP[t-1][w], DP[t-1][w-1]) + 1
            else:
                DP[t][w] = max(DP[t-1][w], DP[t-1][w-1])
        else:
            if w % 2 + 1 == plums[t-1]:
                DP[t][w] = DP[t-1][w] + 1
            else:
                DP[t][w] = DP[t-1][w]
print(max(DP[T]))