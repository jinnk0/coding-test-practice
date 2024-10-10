'''
출처 : 백준 실버2 - 헌내기는 친구가 필요해
알고리즘 분류 : 그래프 이론, 그래프 탐색, BFS/DFS

1 <= N, M <= 600
이동방향 : (1, 0), (0, 1), (-1, 0), (0, -1)
O 빈공간 X 벽 I 도연 P 사람 
'''
import sys
from collections import deque

data = sys.stdin.readlines()
N, M = map(int, data[0].split())
no = ['X', 'I', 'V']

def bfs(n, m):
    queue = deque([[n, m]])
    count = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] not in no:
                if matrix[nx][ny] == 'P':
                    count += 1
                matrix[nx][ny] = 'V'
                queue.append([nx, ny])
    return count

result = 0
matrix = [list(line) for line in data[1:]]
for n in range(N):
    for m in range(M):
        if matrix[n][m] == 'I':
            result = bfs(n, m)
if result == 0:
    print('TT')
else:
    print(result)