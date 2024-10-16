'''
# 출처 : 백준 3758 KCPC
# 문제 유형 : 구현, 정렬
# 입력 
    - T : 테스트 케이스 개수
    - N : 팀의 개수 (3 <= N)
    - k : 문제의 개수 (k <= 100)
    - t : 본인 팀의 ID (1 <= t <= n)
    - m : 로그 엔트리의 개수 (3 <= m <= 10,000)
    - m개의 로그 데이터
        - i : 팀 ID (1 <= i <= n)
        - j : 문제 번호 (1 <= j <= k)
        - s : 점수 (0 <= s <= 100)
# 출력 : 테스트 케이스 별 본인 팀 순위(줄바꿈)
'''
import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, k, t, m = map(int, input().split())

    scores = [[0] * (k + 1) for _ in range(N + 1)]
    submission_count = [0] * (N + 1)
    last_submission_time = [0] * (N + 1)

    for log_index in range(m):
        i, j, s = map(int, input().split())
        if s > scores[i][j]:
            scores[i][j] = s
        submission_count[i] += 1
        last_submission_time[i] = log_index + 1
    
    results = []
    for n in range(1, N + 1):
        total_score = sum(scores[n])
        total_submissions = submission_count[n]
        last_time = last_submission_time[n]
        results.append((total_score, total_submissions, last_time, n))

    results.sort(key=lambda x: (-x[0], x[1], x[2]))

    rank = 1
    for result in results:
        if result[3] == t:
            print(rank)
            break
        rank += 1



        
