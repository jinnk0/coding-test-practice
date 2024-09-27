import sys

input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    prices = list(map(int, input().split()))[::-1]
    max = prices[0]
    profit = 0
    for price in prices:
        if price > max:
            max = price
        else:
            profit += max - price
    print(profit)

