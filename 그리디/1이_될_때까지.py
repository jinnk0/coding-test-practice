N, K = map(int, input().split())
count = 0
while (N >= K):
    if (N % K == 0):
        N //= K
        count += 1
    else:
        N -= 1
        count += 1
if N != 1:
    count += N % K
print(count)