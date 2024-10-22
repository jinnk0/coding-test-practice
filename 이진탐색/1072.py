x, y = map(int, input().split())
z = int(100 * y / x)

start = 0
end = x

answer = -1
while start <= end:
    mid = (start + end) // 2
    new_z = int(100 * (y + mid) / (x + mid))

    if new_z > z:
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)