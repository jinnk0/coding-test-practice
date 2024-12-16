'''
# 출처 : 백준 22233 가희와 키워드
# 유형 : 자료 구조, 문자열, 파싱, 해시시
'''
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
keywords = {}
for _ in range(N):
    keywords[input().strip()] = 1

for _ in range(M):
    posts = list(input().rstrip().split(','))
    for post in posts:
        if post in keywords:
            keywords.pop(post)
    print(len(keywords))