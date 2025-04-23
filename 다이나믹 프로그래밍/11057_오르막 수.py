'''
# 출처 : 백준 11057 오르막 수 (실버1)
# 유형 : 다이나믹 프로그래밍 
# 오르막 수 : 수의 자리가 오름차순을 이루는 수 (같아도 오름차순으로 침)
# 수의 길이 N이 주어질 때 오르막 수의 개수 구하기(0으로 시작 가능)
'''
# 마지막 자릿수보다 작거나 같은 수로 끝나는 N-1 길이의 오르막수 개수 구하기
MOD = 10007
N = int(input())
DP = [[1] * 10 for _ in range(N+1)]
for i in range(2, N+1):
    for j in range(10):
        DP[i][j] = sum(DP[i-1][k] for k in range(j+1)) % MOD

print(sum(DP[N]) % MOD)