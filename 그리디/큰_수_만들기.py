def solution(number, k):
    answer = ''
    stack = []
    n = len(number) - k
    for i in range(len(number)):
        m = n - len(stack)
        while stack and len(number[i+1:]) >= m and stack[-1] < number[i]:
            stack.pop()
            m = n - len(stack)
        stack.append(number[i])
    return answer.join(stack)[:n]
