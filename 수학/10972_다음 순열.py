'''
# 출처 : 백준 10972 다음 순열 (실버 3)
# 유형 : 수학, 조합론
'''
N = int(input())
target = list(map(int, input().split()))

for i in range(-2, -N-1, -1):
    if target[i] < target[i+1]:
        left_large = min(x for x in target[i+1:] if x > target[i])
        idx = target.index(left_large, i+1)
        target[i], target[idx] = target[idx], target[i]
        target[i+1:] = sorted(target[i+1:])
        print(*target)
        break
else:
    print(-1)

