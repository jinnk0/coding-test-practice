'''
# 출처 : 백준 11123 양 한마리... 양 두마리...
# 문제 유형 : 그래프 이론, 그래프 탐색, BFS/DFS
# 입력
    1. 첫째줄 : 테스트 케이스 수 T
    2. 각 테스트 케이스의 첫째줄 : 그리드의 높이 H, 그리드의 너비 W
    3. 각 테스트 케이스의 그리드의 높이 H에 걸쳐서 W개의 문자로 이루어진 문자열
# 출력 : 양 무리의 개수
'''
import sys
from collections import deque

def bfs(i, j, matrix, count, H, W):
    matrix[i][j] = '.'
    queue = deque([(i, j)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if nx >= 0 and nx < H and ny >= 0 and ny < W and matrix[nx][ny] == '#':
                queue.append((nx, ny))
                matrix[nx][ny] = '.'
    return matrix, count+1

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    count = 0
    H, W = map(int, input().split())
    matrix = [list(input()) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if matrix[i][j] == '#':
                matrix, count = bfs(i, j, matrix, count, H, W)
    print(count)