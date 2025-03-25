'''
# 출처 : 백준 10971 외판원 순회 2 (실버2)
# 유형 : 브루트포스, 백트래킹(완전탐색), 외판원 순회 문제(TSP)
'''
import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().strip().split())) for _ in range(N)]

def dfs(start, current, visited, weight, minimum):
    if len(visited) == N:
        if W[current][start] > 0:
            return min(minimum, weight + W[current][start])
        return minimum
    
    for neighbor in range(N):
        if neighbor not in visited and W[current][neighbor] > 0:
            visited.add(neighbor)
            minimum = dfs(start, neighbor, visited, weight + W[current][neighbor], minimum)
            visited.remove(neighbor)
        
    return minimum

minimum = float('inf')

for city in range(N):
    minimum = dfs(city, city, {city}, 0, minimum)

print(minimum)
