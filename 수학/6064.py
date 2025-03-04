'''
# 출처 : 백준 6064 카잉 달력 (실버1)
# 유형 : 수학, 브루트포스, 정수론
'''
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())

    found = False
    year = x
    while year <= M * N: 
        if (year - 1) % N + 1 == y: 
            print(year)
            found = True
            break
        year += M 

    if not found:
        print(-1)
