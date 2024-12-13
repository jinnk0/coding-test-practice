'''
# 출처 : 백준 12847 꿀 아르바이트
# 유형 : 누적 합, 슬라이딩 윈도우
# 입력 
    1. 첫째줄 : 월세 내기 바로 전 날인 n, 일을 할 수 있는 날 m (1 <= n <= 100,000, 0 <= m <= n)
    2. 둘째줄 : 1일부터 n일까지의 일급 T (0 <= T <= 1,000,000)
# 출력 : 준수가 일을 해서 벌 수 있는 최대 이익
'''
n, m = map(int, input().split())
T = list(map(int, input().split()))
profit = sum(T[:m])
profits = [profit]
for i in range(m, n):
    profit -= T[i-m]
    profit += T[i]
    profits.append(profit)
print(max(profits))