from collections import deque
import sys

def bfs(start_x, start_y, matrix, M, N):
    queue = deque([(start_x, start_y)])
    matrix[start_x][start_y] = 0
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < M and 0 <= ny < N and matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                queue.append((nx, ny))

input = sys.stdin.read
data = input().strip().splitlines()

T = int(data[0])
results = []
index = 1

for _ in range(T):
    L = data[index].strip().split()
    M = int(L[0])
    N = int(L[1])
    K = int(L[2])
    matrix = [[0] * N for _ in range(M)]

    for j in range(K):
        x, y = map(int, data[index + 1 + j].split())
        matrix[x][y] = 1
        
    index += K + 1
    answer = 0
        
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1:
                bfs(i, j, matrix, M, N)
                answer += 1
        
    results.append(answer)

for result in results:
    print(result)