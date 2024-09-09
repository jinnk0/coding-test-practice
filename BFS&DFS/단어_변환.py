from collections import deque

def solution(begin, target, words):
    answer = 0
    queue = deque()
    queue.append([begin, 0])
    if target not in words:
        return 0
    while queue:
        begin, count = queue.popleft()
        if begin == target:
            return count
        else:
            for word in words:
                cnt = 0
                for i in range(len(begin)):
                    if begin[i] != word[i]:
                        cnt += 1
                if cnt == 1:
                    queue.append([word, count + 1])
    return answer