'''
# 출처 : 백준 11053 가장 긴 증가하는 부분 수열 (실버2)
# 유형 : 다이나믹 프로그래밍
'''
N = int(input())
numbers = list(map(int, input().split()))

DP = [[1] * (N+1) for _ in range(N+1)]

for j in range(1, N+1):
    for i in range(j+1, N+1):
        if numbers[i-1] > numbers[j-1]:
            DP[i][j] = max(DP[j][j] + 1, max(DP[j]) + 1)

print(max(map(max, DP)))

'''
# 위 방법은 풀리긴하지만, 매우 비효율적
# 2차원 배열 대신 1차원 배열을 사용하되, 최대값을 갱신
'''
N = int(input())
numbers = list(map(int, input().split()))

DP = [1] * N

for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            DP[i] = max(DP[i], DP[j] + 1)

print(max(DP))
