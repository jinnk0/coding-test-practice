'''
# 출처 : 백준 14502 연구소
# 유형 : 구현, 그래프 이론, BFS
# 입력 
    1. 첫째줄 : 지도의 세로 크기 N, 가로 크기 M (3 <= N, M <= 8)
    2. 둘째줄 ~ : N개의 줄에 지도의 모양 (0: 빈칸, 1: 벽, 2: 바이러스)
        - 2 <= 바이러스의 개수 <= 10
        - 빈칸의 개수 >= 3
# 출력 : 얻을 수 있는 안전 영역의 최대 크기
'''
from itertools import combinations
from collections import deque

def bfs(virus, map, N, M):
    queue = deque(virus)
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < M and map[nx][ny] == 0:
                map[nx][ny] = 2
                queue.append((nx, ny))
    return map

N, M = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]
empty = [(x, y) for x in range(N) for y in range(M) if map[x][y] == 0]
virus = [(x, y) for x in range(N) for y in range(M) if map[x][y] == 2]
walls = combinations(empty, 3)

safe_zones = []
for wall in walls:
    temp = [row[:] for row in map]
    for x, y in wall:
        temp[x][y] = 1
    result = bfs(virus, temp, N, M)
    safe_zones.append(sum(row.count(0) for row in temp))

print(max(safe_zones))
    
