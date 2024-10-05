from collections import deque

N, K = map(int, input().split())
queue = deque([i for i in range(N)])

while (len(queue) > 1):
    if len(queue) > K:
        queue.rotate(-1)
        for _ in range(K-1):
            queue.popleft()
    else:
        queue = deque([queue.popleft()])

print(queue.popleft()+1)