'''
# 출처 : 백준 1260 DFS와 BFS (실버2)
# 유형 : 그래프 이론, 그래프 탐색, 너비 우선 탐색, 깊이 우선 탐색
'''
from collections import deque, defaultdict
import sys
input = sys.stdin.readline

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for neighbor in sorted(graph[v]):
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)
    
def bfs(graph, start, visited):
    visited[start] = True
    queue = deque([start])
    print(start, end=' ')
    while queue:
        v = queue.popleft()
        for neighbor in sorted(graph[v]):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                print(neighbor, end=' ')

N, M, V = map(int, input().split())
graph = defaultdict(set)
visited = [False] * (N+1)
for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)

dfs(graph, V, visited)
visited = [False] * (N+1)
print()
bfs(graph, V, visited)
