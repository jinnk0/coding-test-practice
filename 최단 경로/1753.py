import heapq
import sys

input = sys.stdin.read
data = input().splitlines()

V, E = map(int, data[0].split())
start = int(data[1])
graph = [[] for _ in range(V + 1)]
INF = int(1e9)

for i in range(2, E + 2):
    u, v, w = map(int, data[i].split())
    graph[u].append((v, w))

def dijkstra(start):
    dist = [INF] * (V + 1)
    dist[start] = 0
    pq = [(0, start)]
    
    while pq:
        d, node = heapq.heappop(pq)
        
        if dist[node] < d:
            continue
        
        for neighbor, weight in graph[node]:
            cost = d + weight
            if cost < dist[neighbor]:
                dist[neighbor] = cost
                heapq.heappush(pq, (cost, neighbor))
    
    return dist

distances = dijkstra(start)

# 결과 출력
for i in range(1, V + 1):
    if distances[i] == INF:
        print("INF")
    else:
        print(distances[i])
