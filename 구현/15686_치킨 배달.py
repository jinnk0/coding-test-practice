'''
# 백준 골드5 15686 치킨 배달

# 최대 크기가 N x N인 도시의 각 칸을 (r, c)로 나타냄
# 도시의 각 칸은 빈 칸, 치킨집, 집 중 하나
# 치킨 거리 : 집과 가장 가까운 치킨집 사이의 거리
# 도시의 치킨 거리 : 모든 집의 치킨 거리의 합
# 치킨집을 M개만 남기고 없앴을 때 도시의 치킨 거리 최소값 구하기

# 입력 : N(2 <= N <= 50), M(1 <= M <= 13)
# 조건 : 0은 빈칸, 1은 집, 2는 치킨집을 의미 (1 <= 1의 개수 <= 2N, M <= 2의 개수 <= 13)
# 출력 : 도시의 치킨 거리 최솟값
'''
import sys
input = sys.stdin.readline
import itertools

# 도시의 치킨 거리 구하는 함수
def sum_of_chicken_distance(houses, chickens):
    chicken_distance_of_city = 0
    for r1, c1 in houses:
        min_chickend_distance = sys.maxsize
        for r2, c2 in chickens:
            min_chickend_distance = min(min_chickend_distance, abs(r1-r2) + abs(c1-c2))
        chicken_distance_of_city += min_chickend_distance
    return chicken_distance_of_city

n, m = map(int, input().split())

# 모든 집과 치킨집의 위치 구하기
houses = []
chickens = []
minimum_distance = sys.maxsize
for i in range(1, n + 1):
    line = list(map(int, input().split()))
    for j in range(n):
        if line[j] == 1:
            houses.append((i, j+1))
        if line[j] == 2:
            chickens.append((i, j+1))

selected_chickens = itertools.combinations(chickens, m)
for selected_combo in selected_chickens:
    minimum_distance = min(minimum_distance, sum_of_chicken_distance(houses, selected_combo))

print(minimum_distance)
