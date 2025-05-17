'''
# 출처 : 백준 2178 미로 탐색 (실버1)
# 유형 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 격자 그래프
'''
import sys
input = sys.stdin.readline
from collections import deque

def bfs(matrix, start, visited):
    queue = deque([start])
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and matrix[nx][ny] == 1:
                matrix[nx][ny] += matrix[x][y]
                queue.append((nx, ny))

    return matrix

N, M = map(int, input().split())
matrix = [list(map(int, list(input().strip()))) for _ in range(N)]

visited = [[False] * M for _ in range(N)]
matrix = bfs(matrix, (0, 0), visited)
print(matrix[N-1][M-1])
