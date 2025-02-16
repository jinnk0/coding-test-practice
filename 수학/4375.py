'''
# 출처 : 백준 4375 1
# 난이도 : 실버3
# 유형 : 수학, 브루트포스, 정수론
'''
import sys

data = sys.stdin.read().strip()
lines = list(map(int, data.split('\n')))

for line in lines:
    answer = "1"
    while int(answer) % line != 0:
        answer += "1"
    print(len(answer))

