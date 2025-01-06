'''
# 출처 : 백준 2512 예산
# 난이도 : 실버2
# 유형 : 이진탐색
'''
N = int(input())
budgets = list(map(int, input().split()))
M = int(input())

if sum(budgets) <= M:
    print(max(budgets))
else:
    start = 0
    end = max(budgets)
    while start <= end:
        mid = (start + end) // 2
        total = sum(min(mid, budget) for budget in budgets)
        if total <= M:
            result = mid
            start = mid + 1
        else:
            end = mid - 1
    print(end)
