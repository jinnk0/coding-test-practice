import sys

input = sys.stdin.readline
N = int(input())
numbers = [list(map(int, input().split())) for _ in range(N)]
numbers.sort(key=lambda x:(x[1], x[0]))
print('\n'.join(' '.join(map(str, number)) for number in numbers))