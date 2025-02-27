'''
# 출처 : 백준 1476 날짜 계산 (실버 5)
# 유형 : 수학, 정수론, 브루트포스
'''
E, S, M = map(int, input().split())

e, s, m = 1, 1, 1
year = 1

while e != E or s != S or m != M:
    year += 1
    e += 1
    s += 1
    m += 1
    if year % 15 == 1:
        e -= 15
    if year % 28 == 1:
        s -= 28
    if year % 19 == 1:
        m -= 19

print(year)
