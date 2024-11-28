'''
# 출처 : 백준 13305 주유소
# 문제 유형 : 그리디
# 입력 
    - N : 도시 개수 (2 <= N <= 100,000)
    - distance : 인접한 두 도시를 연결하는 도로의 길이 (N-1개) (1 <= distance <= 1,000,000,000)
    - 도시의 주유소 리터 당 가격 (N개)
# 출력 : 제일 왼쪽 도시부터 제일 오른쪽 도시까지 이동하는 동안 주유하는 기름의 최소 비용
'''
N = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

cost = 0
min = prices[0]
for i in range(len(distances)):
    if prices[i] < min:
        min = prices[i]
    cost += min * distances[i]

print(cost)