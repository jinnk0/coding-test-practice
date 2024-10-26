N = int(input())
K = list(map(int, input().split()))

DP = [0] * (N + 1)
DP[1] = K[0]
DP[2] = max(K[1], K[2])
for i in range(2, N+1):
    DP[i] = max(DP[i-1], DP[i-2] + K[i-1])
print(DP[N])