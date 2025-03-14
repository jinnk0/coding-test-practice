N = int(input())

DP = [0] * (N + 1)
DP[1] = 1
DP[2] = 3
for i in range(3, N+1):
    DP[i] = (DP[i-1] + 2 * DP[i-2]) % 796796

print(DP[N])