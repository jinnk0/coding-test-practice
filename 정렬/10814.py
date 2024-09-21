import sys

input = sys.stdin.readline
N = int(input())
members = [(int(data[0]), data[1]) for data in (input().split() for _ in range(N))]
members.sort(key=lambda x:x[0])
print('\n'.join(' '.join(map(str, member)) for member in members))
