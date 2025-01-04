n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
result = []
current = 1
possible = True

for number in sequence:
    while current <= number:
        stack.append(current)
        result.append("+")
        current += 1
    
    if stack[-1] == number:
        stack.pop()
        result.append("-")
    else:
        possible = False
        break

if possible:
    print("\n".join(result))
else:
    print("NO")
