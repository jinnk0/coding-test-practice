# 출처 : 이것이 코딩테스트다

import sys
from collections import deque

def bfs(matrix, N, M):
    queue = deque()
    queue.append([0, 0])
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])

    return matrix[N-1][M-1]

data = sys.stdin.readlines()
N, M = map(int, data[0].split())
matrix = []
for n in range(1, N+1):
    row = [int(data[n][i]) for i in range(M)]
    matrix.append(row)

print(bfs(matrix, N, M))