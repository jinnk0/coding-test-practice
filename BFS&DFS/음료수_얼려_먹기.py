# 출처 : 이것이 코딩 테스트다

from collections import deque
import sys

def bfs(n, m, matrix):
    queue = deque()
    queue.append([n, m])
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
                matrix[nx][ny] = 1
                queue.append([nx, ny])

    return matrix

data = sys.stdin.readlines()
N, M = map(int, data[0].split())
matrix = []
for n in range(1, N+1):
    row = [int(data[n][i]) for i in range(M)]
    matrix.append(row)
count = 0
for n in range(N):
    for m in range(M):
        if matrix[n][m] == 0:
            matrix[n][m] = 1
            matrix = bfs(n, m, matrix)
            count += 1

print(count)