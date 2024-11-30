'''
# 출처 : 백준 1946 신입 사원
# 문제 유형 : 그리디
# 입력
    - T : 테스트 케이스 수 (1 <= T <= 20)
    - N : 지원자의 수 (1 <= N <= 100,000)
    - 서류심사 성적의 순위, 면접 성적의 순위 (x N개, 동석차 없음)
# 출력 : 둘 다 다른 지원자보다 낮은 경우 선발하지 않을 때 뽑을 수 있는 최대 인원
'''
import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    count = 1
    N = int(input())
    grades = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x : x[0])
    rank = grades[0][1]
    for grade in grades:
        if rank > grade[1]:
            rank = grade[1]
            count += 1

    print(count)