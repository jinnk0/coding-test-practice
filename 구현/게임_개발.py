N, M = map(int, input().split())
a, b, d = map(int, input().split())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
direct = [[0, -1], [-1, 0], [0, 1], [1, 0]]

def move(a, b, d, cnt, matrix):
    matrix[b][a] = 1
    if end(matrix, a, b):
        return cnt
    da, db = direct[d]
    na = a + da
    nb = b + db
    if 0 <= na < N and 0 <= nb < M and matrix[nb][na] == 0:
        return move(na, nb, (d+4-1)%4, cnt+1, matrix)
    else:
        return move(a, b, (d+4-1)%4, cnt, matrix)

def end(matrix, a, b):
    for da, db in direct:
        na = a + da
        nb = b + db
        if 0 <= na < N and 0 <= nb < M and matrix[nb][na] == 0:
            return False
    return True

print(move(a, b, d, 1, matrix))