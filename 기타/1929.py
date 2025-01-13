'''
# 출처 : 백준 1929 소수 구하기
# 난이도  : 실버 3
# 유형 : 수학
'''
M, N = map(int, input().split())

numbers = [i for i in range(N+1)]
numbers[1] = 0

for number in numbers:
    if number != 0:
        i = 2
        while number * i <= N:
            numbers[number * i] = 0
            i += 1
        if number >= M:
            print(number)
