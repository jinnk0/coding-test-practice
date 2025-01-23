import sys
import heapq
input = sys.stdin.readline

N = int(input())
commands = [int(input()) for _ in range(N)]

max_heap = []

for command in commands:
    if command == 0:
        if max_heap:
            print(-heapq.heappop(max_heap))
        else:
            print(0)
    else:
        heapq.heappush(max_heap, -command)
