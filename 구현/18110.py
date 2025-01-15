'''
# 출처 : 백준 18110 solved.ac
# 난이도 : 실버4
# 유형 : 구현, 수학, 정렬
'''
import sys
input = sys.stdin.readline

def roundUp(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

N = int(input())
numbers = [int(input()) for _ in range(N)]
numbers.sort()
cut = roundUp(N * 0.15)
if cut == 0:
    select = numbers
else:
    select = numbers[cut:-cut]
if len(select) == 0:
    print(0)
else:
    print(roundUp(sum(select) / len(select)))