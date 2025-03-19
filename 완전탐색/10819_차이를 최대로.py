'''
# 출처 : 백준 10891 차이를 최대로 (실버2)
# 유형 : 브루트포스, 백트래킹(완전탐색)
'''
# 가능한 모든 순열 구하기
# 차이의 최대값 구하기

from itertools import permutations

N = int(input())
numbers = list(map(int, input().split()))

cases = list(permutations(numbers, N)) # 가능한 모든 순열 구하기

max_diff = - 999
for case in cases:
    diff = 0
    for i in range(len(case)-1):
        diff += abs(case[i] - case[i+1])
    max_diff = max(max_diff, diff) # 차이의 최대값 저장 

print(max_diff)

'''
# 다른 방법

# 가능한 모든 순열의 차이의 최대값 탐색 (백트래킹 dfs 이용)
'''
N = int(input())
numbers = list(map(int, input().split()))

def dfs(depth, prev, visited, diff_sum, max_diff):
    if depth == N:
        return max(diff_sum, max_diff)
    
    diff = -float('inf')
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            diff = max(diff, dfs(depth+1, numbers[i], visited, diff_sum + abs(prev - numbers[i]), max_diff))
            visited[i] = False
        
    return diff
            
max_diff = -999
for i in range(N):
    visited = [False] * N
    visited[i] = True
    max_diff = dfs(1, numbers[i], visited, 0, max_diff)

print(max_diff)


