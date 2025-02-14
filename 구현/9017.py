'''
# 출처 : 백준 9017 크로스 컨트리
# 난이도 : 실버 3
# 유형 : 구현
'''
from collections import defaultdict

T = int(input())
for _ in range(T):
    teams = defaultdict(list)
    score = 1
    N = int(input())
    numbers = list(map(int, input().split()))
    for number in numbers:
        if number in teams.keys():
            teams[number].append(score)
            score += 1
        elif numbers.count(number) == 6:
            teams[number].append(score)
            score += 1
    min_score = N*6
    winner = 0
    for team in teams.keys():
        score = sum(teams[team][:4])
        if score < min_score:
            min_score = score
            winner = team
        elif score == min_score:
            if teams[team][4] < teams[winner][4]:
                winner = team

    print(winner)