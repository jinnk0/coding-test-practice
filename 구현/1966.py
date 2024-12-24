'''
# 출처 : 백준 1966 프린터 큐
# 유형 : 구현, 자료구조, 시뮬레이션, 큐
# 입력
    1. 첫 줄 : 테스트 케이스의 수 T
    2. 테스트 케이스의 첫 줄 : 문서의 개수 N (1 <= N <= 100), target 문서의 위치 M (0 <= M < M)
    3. 테스트 케이스의 둘째줄 : 문서의 중요도 순서대로
# 출력 : target 문서가 출력되는 순서
'''
from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    queue = deque(map(int, input().split()))

    index = M
    count = 0

    while queue:
        if queue[0] == max(queue):
            queue.popleft()
            count += 1
            if index == 0:
                print(count)
                break
            else:
                index -= 1
        else:
            queue.rotate(-1)
            if index == 0:
                index = len(queue) - 1
            else:
                index -= 1

