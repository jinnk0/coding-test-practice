'''
# 출처 : 백준 11724 연결 요소의 개수 (실버2)
# 유형 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
'''
import sys
from collections import defaultdict, deque
input = sys.stdin.readline

def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for neighbor in sorted(graph[v]):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return 1

N, M = map(int, input().split())
conn = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    conn[u].append(v)
    conn[v].append(u)

visited = [False] * (N+1)
count = 0
for i in range(1, N+1):
    if not visited[i]:
        count += bfs(conn, i, visited)

print(count)