from collections import deque

def solution(s):
    queue = deque()
    for s_ in s:
        if s_ == ')':
            if queue and queue[0] == '(':
                queue.popleft()
            else:
                return False
        else:
            queue.append(s_)

    return len(queue) == 0

s = input()
solution(s)