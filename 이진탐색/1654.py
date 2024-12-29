import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lengths = []
for _ in range(K):
    lengths.append(int(input()))

start = 1
end = max(lengths)

while start <= end:
    mid = (start + end) // 2
    count = sum(length // mid for length in lengths)
    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end) 