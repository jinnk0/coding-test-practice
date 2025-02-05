'''
# 출처 : 백준 28353 고양이 카페
# 난이도 : 실버3
# 유형 : 그리디, 정렬, 투 포인터
'''
N, K = map(int, input().split())
weights = sorted(list(map(int, input().split())))
left = 0
right = N-1
count = 0
while left < right:
    if weights[left] + weights[right] <= K:
        count += 1
        left += 1
        right -= 1
    else:
        right -= 1
    
print(count)