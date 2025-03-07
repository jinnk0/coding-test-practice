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


'''
# 다른 풀이(중국인의 나머지 정리)

import sys
from math import gcd

def extended_gcd(a, b):
    """확장된 유클리드 알고리즘을 이용해 ax ≡ 1 (mod b)의 해 x를 찾음"""
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

def solve(M, N, x, y):
    """중국인의 나머지 정리를 이용해 최소의 year 찾기"""
    # (x, y)에서 x와 y를 1-based index에서 0-based index로 변환
    x -= 1
    y -= 1

    # M * k ≡ (y - x) (mod N) 풀기
    g, m_inv, _ = extended_gcd(M, N)

    # 해가 존재하지 않는 경우
    if (y - x) % g != 0:
        return -1

    # k 계산 (M의 역원을 곱해서 (y - x) / g를 찾기)
    k = ((y - x) // g * m_inv) % (N // g)

    # year 계산
    year = M * k + x + 1  # 다시 1-based index로 변환

    return year

# 입력 처리
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(solve(M, N, x, y))
'''
