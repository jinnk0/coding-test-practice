N = int(input())
parts = sorted(list(map(int, input().split())))
M = int(input())
requested_parts = list(map(int, input().split()))

def binary_search(arr, part, i, j):
    while i <= j:
        m = (i + j) // 2
        if arr[m] == part:
            return True
        elif arr[m] > part:
            j = m - 1
        else:
            i = m + 1
    return False

# 각 요청 부품 번호를 확인하여 결과 출력
for part in requested_parts:
    if binary_search(parts, part, 0, len(parts) - 1):
        print("yes", end=' ')
    else:
        print("no", end=' ')
