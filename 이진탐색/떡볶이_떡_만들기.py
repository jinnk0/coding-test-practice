'''
# 출처 : 이것이 코딩테스트다
# 문제 유형 : 이진탐색
# 입력 형태
    N, M
    n1, n2, n3, ...
    - N : 떡의 개수(1 <= N <= 1,000,000)
    - M : 떡의 길이(1 <= M <= 2,000,000,000)
    - n1, n2, n3, ... : 떡들의 길이
# 출력 : 최소 M만큼의 떡을 가져가기 위해 절단기에 설정할 최대 높이
'''
N, M = map(int, input().split())
lengths = list(map(int, input().split()))
result = 0

start = 0
end = max(lengths)
while start <= end:
    total = 0
    mid = (start + end) // 2
    for length in lengths:
        if length > mid:
            total += length - mid
    if total < M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)