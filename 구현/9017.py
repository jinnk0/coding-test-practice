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
    result = list(teams.keys())
    result.sort(key=lambda x : (sum(teams[x][:4]), teams[x][4]))

    print(result[0])