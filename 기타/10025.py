'''
# 출처 : 백준 10025 게으른 백곰
# 유형 : 누적 합, 투 포인터, 슬라이딩 윈도우
# 입력 
    1. 첫 줄 : 양동이의 수 N(1 <= N <= 100,000), 도달 가능한 거리 K (1 <= K <= 2,000,000)
    2. 둘째 줄 ~ : N개의 양동이 안의 얼음의 양 g(1 <= g <= 10,000), 양동이의 좌표 x(1 <= x <= 1,000,000)
# 출력 : 자리 잡은 좌표에서 도달 가능한 얼음의 양의 최댓값
'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
matrix = [0] * 1000001
last_pos = 0
for _ in range(N):
    g, x = map(int, input().split())
    matrix[x] = g

    last_pos = max(last_pos, x)

window_size = 2 * K + 1
window_sum = sum(matrix[:window_size])
answer = window_sum

for end in range(window_size, last_pos+1):
    window_sum += matrix[end] - matrix[end-window_size]
    answer = max(answer, window_sum)

print(answer)