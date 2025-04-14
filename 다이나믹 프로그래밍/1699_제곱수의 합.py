'''
# 출처 : 백준 1699 제곱수의 합 (실버2)
# 유형 : 다이나믹 프로그래밍
# 자연수 N을 제곱수들의 합으로 나타낼 때 항의 최소개수 구하기 
'''
# 자연수 N이 가질 수 있는 제곱수를 모두 고려
# 자연수 N - 제곱수가 가지는 항의 최소 개수 + 1
N = int(input())
DP = [100000] * (N+1)
DP[0], DP[1] = 0, 1
for i in range(2, N+1):
    for j in range(1, int(i**0.5)+1):
        DP[i] = min(DP[i], DP[i-j**2] + 1)

print(DP[N])
