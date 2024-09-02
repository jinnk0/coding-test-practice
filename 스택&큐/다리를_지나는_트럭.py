from collections import deque

def solution(bridge_length, weight, truck_weights):
    second = 0
    arrive = 0
    weight_sum = 0
    queue = deque([0] * bridge_length)
    N = len(truck_weights)
    for truck in truck_weights:
        weight_sum -= queue.popleft()
        while weight_sum + truck > weight:
            queue.append(0)
            weight_sum -= queue.popleft()
            second += 1
        else:
            queue.append(truck)
            weight_sum += truck
        second += 1
    return second + bridge_length