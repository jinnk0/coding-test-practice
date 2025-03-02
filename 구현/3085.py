'''
# 출처 : 백준 3085 사탕 게임 (실버2)
# 유형 : 구현, 브루트포스
'''
import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(input().strip()) for _ in range(N)]

def count_maximum(matrix):
    maximum = 1
    for i in range(N):
        pre = ""
        cont = []
        for j in range(N):
            if matrix[i][j] != pre:
                cont = []
            pre = matrix[i][j]
            cont.append(matrix[i][j])
            maximum = max(maximum, len(cont))
    
    for j in range(N):
        pre = ""
        cont = []
        for i in range(N):
            if matrix[i][j] != pre:
                cont = []
            pre = matrix[i][j]
            cont.append(matrix[i][j])
            maximum = max(maximum, len(cont))
    return maximum

maximum = count_maximum(matrix)
if maximum == N:
    print(N)
else:
    for i in range(N):
        for j in range(N-1):
            if matrix[i][j] != matrix[i][j+1]:
                matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]
                maximum = max(maximum, count_maximum(matrix))
                matrix[i][j], matrix[i][j+1] = matrix[i][j+1], matrix[i][j]

    for j in range(N):
        for i in range(N-1):
            if matrix[i][j] != matrix[i+1][j]:
                matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]
                maximum = max(maximum, count_maximum(matrix))
                matrix[i][j], matrix[i+1][j] = matrix[i+1][j], matrix[i][j]
    print(maximum)


        