'''
# 출처 : 백준 1181 단어 정렬
# 난이도 : 실버5
# 유형 : 문자열, 정렬
'''
import sys
input =  sys.stdin.readline

N = int(input())
words = list(set([input().strip() for _ in range(N)]))

words.sort(key=lambda x : (len(x), x))

print('\n'.join(words))
