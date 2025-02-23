'''
# 출처 : 백준 17427 약수의 합 2
# 난이도 : 실버 2
# 유형 : 수학, 정수론
'''
N = int(input())

sum_divisors = [0] * (N + 1)

for i in range(1, N + 1):
    for j in range(i, N + 1, i):
        sum_divisors[j] += i

print(sum(sum_divisors))
