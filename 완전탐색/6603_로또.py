'''
# 출처 : 백준 6603 로또 (실버2)
# 유형 : 수학, 조합론, 백트래킹, 재귀
'''
from itertools import combinations
import sys

input = sys.stdin.readline

while True:
    line = input().strip()
    if line == "0":
        break

    _, *S = line.split()
    for case in combinations(S, 6):
        print(' '.join(case))

    print()