'''
# 출처 : 백준 11052 카드 구매하기 (실버1)
# 유형 : 다이나믹 프로그래밍
# 1 ~ N개의 카드가 들어있는 카드팩
# 가격을 최대로 지불하여 N개의 카드를 구매
'''
N = int(input())
prices = list(map(int, input().split()))
DP = [0] * (N + 1)
DP[1] = prices[0]

for i in range(2, N+1):
    DP[i] = max(max(DP[j] + DP[i-j] for j in range(1, N//2+1)), prices[i-1])

print(DP[N])