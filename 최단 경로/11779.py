'''
# 출처 : 백준 11779 최소비용 구하기 2
# 문제 유형 : 최단 경로, 다익스트라
# 입력
    1. 첫 번째 줄: 도시(노드)의 개수 n (1 ≤ n ≤ 1000)
    2. 두 번째 줄: 버스(간선)의 개수 m (1 ≤ m ≤ 100,000)
    3. 이후 m개의 줄: 각 줄에 u v w가 주어짐 (u → 출발지, v → 도착지, w → 비용)
    4. 마지막 줄: 출발 도시 start와 도착 도시 end.
# 출력 
    1. start에서 end까지의 최소 비용
    2. 최소 비용 경로에 포함된 도시의 수
    3. 최소 비용 경로에 포함된 도시들
'''
import sys
import heapq

def dijkstra(start, end):
    dist = [float('inf')] * (n + 1)
    parent = [-1] * (n + 1)
    dist[start] = 0
    queue = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if current_dist > dist[current_node]:
            continue

        for neighbor_node, cost in graph[current_node]:
            cost = current_dist + cost
            if cost < dist[neighbor_node]: # current_node를 거쳐 가는게 비용이 적음
                dist[neighbor_node] = cost
                parent[neighbor_node] = current_node # neighbor_node를 최단 비용으로 가기 위해서 current_node를 거쳐야 함
                heapq.heappush(queue, (cost, neighbor_node))

    path = []
    node = end
    while node != -1:
        path.append(node)
        node = parent[node]
    path.reverse()

    return dist[end], path

input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())
distance, path = dijkstra(start, end)

print(distance)
print(len(path))
print(' '.join(map(str, path)))
