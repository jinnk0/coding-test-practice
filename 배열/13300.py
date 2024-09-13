N, K = map(int, input().split())
students = [[0]*6 for _ in range(2)]

count = 0
for i in range(N):
    S, Y = map(int, input().split())
    students[S][Y-1] += 1

for group in students:
    for student in group:
        count += (student-1)//K + 1

print(count)