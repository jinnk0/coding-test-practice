'''
# 출처 : 백준 2667 단지번호붙이기
# 유형 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색, 격자 그래프, 플러드 필
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start):
    queue = deque([start])
    movements = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    graph[start[0]][start[1]] = '0'
    count = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in movements:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == '1':
                graph[nx][ny] = '0'
                count += 1
                queue.append((nx, ny))
    
    return count

n = int(input())
graph = [list(input().strip()) for _ in range(n)]

answer = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            answer.append(bfs(graph, (i, j)))

print(len(answer))
print('\n'.join(map(str, sorted(answer))))
