import sys

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[999] * (N + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    graph[i][i] = 0

for _ in range(M):
    A, B = map(int, input().split())
    graph[A][B] = 1
    graph[B][A] = 1

X, K = map(int, input().split())

for i in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

distance = graph[1][K] + graph[K][X]

if distance >= 999:
    print("-1")
else:
    print(distance)