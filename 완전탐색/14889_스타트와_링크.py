'''
# 출처 : 백준 14889 스타트와 링크 (실버1)
# 유형 : 브루트포스, 백트래킹(완전탐색)
'''
from itertools import combinations
import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().strip().split())) for _ in range(N)]

players = list(range(N))

min_diff = float('inf')

for start_team in combinations(players, N//2):
    link_team = list(set(players) - set(start_team))

    start_score = sum(S[i][j] for i in start_team for j in start_team if i != j)
    link_score = sum(S[i][j] for i in link_team for j in link_team if i != j)
    
    min_diff = min(min_diff, abs(start_score - link_score))

print(min_diff)
