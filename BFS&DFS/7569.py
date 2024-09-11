import sys
from collections import deque

def bfs(queue, H, N, M, matrix):
    cnt = -1
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            h, n, m = queue.popleft()
            for dh, dn, dm in [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]:
                _h, _n, _m = h + dh, n + dn, m + dm
                if 0 <= _h < H and 0 <= _n < N and 0 <= _m < M:
                    if matrix[_h][_n][_m] == 0:
                        matrix[_h][_n][_m] = 1
                        queue.append([_h, _n, _m])
        
    for h in range(H):
        for n in range(N):
            if 0 in matrix[h][n]:
                return -1    
        
    return cnt
        
input = sys.stdin.read
data = input().splitlines()

M, N, H = map(int, data[0].split())
matrix = []
index = 1
queue = deque()

for h in range(H):
    area = []
    for n in range(N):
        line = list(map(int, data[index].split()))
        for m in range(M):
            if line[m] == 1:
                queue.append([h, n, m])
        area.append(line)
        index += 1
    matrix.append(area)

print(bfs(queue, H, N, M, matrix))



    
            

