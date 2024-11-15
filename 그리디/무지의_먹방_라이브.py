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
