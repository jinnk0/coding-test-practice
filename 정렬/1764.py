import sys
input = sys.stdin.readline

N, M = map(int, input().split())
notheard = [input().strip() for _ in range(N)]
notsee = [input().strip() for _ in range(M)]

notheard = set(notheard)
notsee = set(notsee)

intersect = sorted(notheard.intersection(notsee))
print(len(intersect))
print('\n'.join(map(str, intersect)))
