'''
# 출처 : 백준 11866 요세푸스 문제 0
# 난이도 : 실버4
# 유형 : 구현, 자료 구조, 큐큐
'''
from collections import deque

N, K = map(int, input().split())
numbers = deque([i for i in range(1, N+1)])
josephus = []
while numbers:
    numbers.rotate(-K+1)
    josephus.append(numbers.popleft())

result = "<" + ", ".join(map(str, josephus)) + ">"
print(result)