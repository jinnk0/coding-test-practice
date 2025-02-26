'''
# 출처 : 백준 6588 골드바흐의 추측 (실버 1)
# 유형 : 수학, 정수론, 소수 판정, 에라토스테네스의 체
'''
import sys
input = sys.stdin.readline

verify = [True] * 1000001
for i in range(2, int(1000000**0.5) + 1): 
        if verify[i] == True:
            for j in range(i+i, 1000001, i):
                verify[j] = False

primes = [i for i in range(3, 1000001) if verify[i] == True] 

while True:
    n = int(input())
    
    if n == 0:
        break

    for prime in primes:
        if prime > n // 2:
            print("Goldbach's conjecture is wrong.")
            break
        if verify[n - prime]:
            print(f"{n} = {prime} + {n - prime}")
            break