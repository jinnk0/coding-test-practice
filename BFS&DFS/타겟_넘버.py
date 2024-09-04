def solution(numbers, target):
    answer = 0
    def dfs(index, sum_number):
        if index == len(numbers):
            if sum_number == target:
                return 1
            else:
                return 0
        return dfs(index + 1, sum_number + numbers[index]) + dfs(index + 1, sum_number - numbers[index])
    answer = dfs(0, 0)
    return answer