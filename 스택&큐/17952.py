import sys

input = sys.stdin.readline
N = int(input())
stack = []
score = 0
for i in range(N):
    task = list(map(int, input().split()))
    if task[0] == 1:
        if task[2] == 1:
            score += task[1]
        else:
            stack.append([task[1], task[2]-1])
    else:
        if stack:
            if stack[-1][1] > 1:
                stack[-1][1] -= 1
            else:
                score += stack.pop()[0]

print(score)