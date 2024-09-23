N, M, K = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
count = M//(K+1)*K + M % (K+1)
print(numbers[-1]*count + numbers[-2]*(M-count))