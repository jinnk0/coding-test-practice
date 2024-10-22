'''
# 출처 : 백준 19637
# 문제 유형 : 이진탐색
# 입력
    N M
    title power (x N)
    stat (x M)
    - N : 칭호의 개수(1 <= N <= 100,000)
    - M : 칭호를 출력해야 하는 캐릭터 개수 (1 <= M <= 100,000)
    - title : 칭호 이름
    - power : 칭호의 전투력 상한값
    - stat : 캐릭터 전투력
# 출력
    캐릭터 전투력에 따른 칭호 (x M)
'''
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
titles = []
powers = []
for _ in range(N):
    title, power = input().split()
    titles.append(title)
    powers.append(int(power))

for _ in range(M):
    stat = int(input())
    start, end = 0, N-1
    while start <= end:
        mid = (start + end) // 2
        if powers[mid] >= stat:
            end = mid -1
        else:
            start = mid + 1
    print(titles[start])
