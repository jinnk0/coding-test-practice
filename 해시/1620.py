'''
# 출처 : 백준 1620 포켓몬 마스터 이다솜
# 난이도 : 실버4
# 유형 : 자료 구조, 해시시
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
word2num = {}
num2word = {}
for i in range(1, N+1):
    name = input().strip()
    word2num[name] = i
    num2word[f'{i}'] = name

for _ in range(M):
    problem = input().strip()
    if problem in word2num.keys():
        print(word2num[problem])
    else:
        print(num2word[problem])