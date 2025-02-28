'''
# 출처 : 백준 1748 수 이어 쓰기 1 (실버4)
# 유형 : 수학, 구현
'''
N = int(input())

length = 0
digit = 1
start = 1

while start <= N:
    end = min(N, start * 10 - 1)
    count = end - start + 1
    length += count * digit
    start *= 10
    digit += 1

print(length)
