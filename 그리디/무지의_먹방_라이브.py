'''
# 프로그래머스 lv.4 무지의 먹방 라이브

# 회전판 위에 N개의 음식 (각 음식의 번호는 1 ~ N)
# 각 음식 섭취에 일정 시간 소요

1. 무지는 1번 음식부터 1초씩 먹기 시작
2. 회전판은 번호가 증가하는 순서대로 다음 음식 운반(원형 회전판)
3. 회전판이 이동하는 데 걸리는 시간은 고려하지 않음

# 무지의 먹방 라이브가 시작한 지 K초 후에 방송 중단
# 방송 재개 시 몇 번 음식부터 먹어야 하는지 반환
# 더 섭취해야할 음식이 없다면 -1 반환

# 입력 : 각 음식을 섭취하는 데 걸리는 시간이 담긴 배열 food_times, K
# 출력 : 방송 재개 시 몇 번 음식부터 먹어야 하는지 (answer)
'''

# 1회차 풀이
def solution(food_times, k):
    N = len(food_times)
    foods = sorted([(food, i) for i, food in enumerate(food_times)], key=lambda x:x[0])
    total_time = 0
    spend_time = 0
  
    if sum(food_times) <= k:
        return -1
      
    for i in range(N):
        time = foods[i][0] - spend_time
        if time * (N - i) <= k - total_time:
            total_time += time * (N - i)
            spend_time = foods[i][0]
        else:
            break
          
    left_foods = sorted(foods[i:], key=lambda x:x[1])
    left_time = (k - total_time) % len(left_foods)
  
    return left_foods[left_time][1] + 1

# 2회차 풀이
# 회전판이 돌아가는 것을 시뮬레이션처럼 계산하여 풀려고 시도했으나 일부 정답 불일치 및 시간 초과로 오답
# 해결 방법 : 각 음식의 섭취 시간을 블록 처럼 생각할 것, 최소힙 사용
import heapq

def solution(food_times, k):
    answer = 0
    # food_times 배열의 원소를 모두 합친 값이 k보다 작을 경우 -1 반환
    if sum(food_times) <= k:
        return -1
    
    # 음식 섭취 시간과 음식 번호를 최소힙을 사용하여 시간 기준 오름차순 정렬
    hq = []
    for i in range(len(food_times)):
        heapq.heappush(hq, (food_times[i], i + 1))

    # remains = 남은 음식 개수
    remains = len(food_times)
    # previous = 이전 층에서 제거한 음식 섭취 시간
    previous = 0

    while hq:
        # now = 현재 힙에 남아 있는 음식 중 가장 작은 음식 섭취 시간 (hq[0][0])
        now = hq[0][0]
        # spend = (now - previous) * remains 최소힙에서 음식을 제거하기 위해 소요되는 시간
        spend = (now - previous) * remains
        
        # k >= spend 이면 최소힙에서 음식 제거
        if k >= spend:
            k -= spend
            heapq.heappop(hq)
            previous = now
            remains -= 1
        # k < spend 이면 음식 번호 순서대로 재정렬 후 k % remains번째 음식의 번호 반환
        else:
            result = sorted(hq, key=lambda x:x[1])
            return result[k%remains][1]
    return -1