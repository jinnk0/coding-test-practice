from collections import deque

def bfs(start_x, start_y, matrix, RGB, N):
    queue = deque([(start_x, start_y)])
    matrix[start_x][start_y] = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 0 \
            and RGB[nx][ny] == RGB[start_x][start_y]:
                matrix[nx][ny] = 1
                queue.append((nx, ny))


N = int(input())
index = 1
RGB = []
RB = []
matrix = [[0]* N for _ in range(N)]
matrix_rb = [[0]* N for _ in range(N)]

area = 0
area_rb = 0

for _ in range(N):
    line = list(input().strip())
    RGB.append(line)
    RB.append(['R' if color == 'G' else color for color in line])
    index += 1

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 0:
            bfs(i, j, matrix, RGB, N)
            area += 1
        if matrix_rb[i][j] == 0:
            bfs(i, j, matrix_rb, RB, N)
            area_rb += 1

print(area, area_rb)


