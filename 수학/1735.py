'''
# 출처 : 백준 1735 분수 합
# 난이도 : 실버 3
# 유형 : 수학, 정수론, 유클리드 호제법
'''
import math

A = [0] * 2
B = [0] * 2
A[0], B[0] = map(int, input().split())
A[1], B[1] = map(int, input().split())

numberA = A[0] * B[1] + A[1] * B[0] 
numberB = B[0] * B[1]
GCD = math.gcd(numberA, numberB)

print(numberA // GCD, numberB // GCD)