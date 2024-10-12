'''
# 출처 : 백준 2606 - 바이러스
# 문제 유형 : 그래프 이론, 그래프 탐색, BFS/DFS
# 입력
    - N : 컴퓨터수(0 < N <= 100) 
    - P : 직접 연결되어 있는 컴퓨터 쌍의 수
    - X, Y : P개의 연결된 컴퓨터 번호 쌍
# 출력 : 1번 컴퓨터를 통해 바이러스에 걸리게 되는 컴퓨터의 수
# 변수 
    - graph : 컴퓨터 연결 쌍 저장
    - visit : 방문한 노드 저장(방문 1 미방문 0)
    - count : 바이러스에 감염된 컴퓨터 수
'''
N = int(input())
P = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(P):
    X, Y = map(int, input().split())
    graph[X].append(Y)
    graph[Y].append(X)
visit = [0] * (N+1)

def dfs(node):
    count = 0
    visit[node] = 1
    for neighbor in graph[node]:
        if visit[neighbor] == 0:
            count += 1
            count += dfs(neighbor)
    return count

print(dfs(1))




