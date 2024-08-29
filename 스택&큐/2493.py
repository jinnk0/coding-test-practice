N = int(input())

heights = list(map(int, input().split()))
answer = []
stack = []

for i in range(N):
    while stack and heights[stack[-1]] < heights[i]:
        stack.pop()
        
    if stack:
        answer.append(str(stack[-1]+1))
    else:
        answer.append('0')
        
    stack.append(i)
    
    
print(' '.join(answer))
    