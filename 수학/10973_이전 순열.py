'''
# 출처 : 백준 10973 이전 순열 (실버3)
# 유형 : 수학, 구현, 조합론

# 뒤에서부터 탐색하면서 처음 감소하는 지점을 찾고, 
# 해당 부분을 적절한 값으로 교체한 뒤 
# 나머지 뒷 부분은 내림차순으로 정렬하는 것이 문제 해결의 핵심 
'''
N = int(input())
target = list(map(int, input().split()))

for i in range(N-1, 0, -1): # 뒤에서부터 탐색 
    if target[i-1] > target[i]: # 처음 감소하는 지점 찾기

        # 적절한 값으로 교체 (target[i-1]보다 작은 값들 중 가장 큰 값) 
        left_small = max(x for x in target[i:] if x < target[i-1]) 
        idx = target.index(left_small, i)
        target[i-1], target[idx] = target[idx], target[i-1]

        target[i:] = sorted(target[i:], reverse=True) # 나머지 부분 내림차순 정렬 
        print(*target)
        break
else:
    print(-1)

'''
# bisect 모듈을 활용한 이진 탐색 방법
# 기본적인 핵심 로직은 같음
# 적절한 값으로 교체하고, 뒷 부분은 내림차순으로 정렬하는 과정 최적화
'''
import bisect 

N = int(input())
target = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if target[i-1] > target[i]: # 여기까진 동일 

        # 뒷 부분 먼저 오름차순 정렬 (bisect 모듈을 사용하기 위해 필요요)
        suffix = sorted(target[i:])

        # 교체할 적절한 값 찾기 (target[i-1]보다 작은 값들 중 가장 큰 값)
        idx = bisect.bisect_left(suffix, target[i-1]) - 1
        left_small = suffix[idx]
        swap_idx = target.index(left_small, i)
        target[i-1], target[swap_idx] = target[swap_idx], target[i-1]

        # 뒷 부분 다시 내림차순 정렬
        target[i:] = sorted(target[i:], reverse=True)
        print(*target)
        break
else:
    print(-1)
