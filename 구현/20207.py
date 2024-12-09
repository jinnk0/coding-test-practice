'''
# 출처 : 백준 20207 달력
# 문제 유형 : 구현, 그리디, 정렬
# 입력 
    1. 첫째줄 : 일정의 개수 N (1 <= N <= 1000)
    2. 둘째줄 : 일정의 개수만큼 시작 날짜 S, 종료 날짜 E (1 <= S <= E <= 365)
# 출력 : 코팅지의 면적
'''
import sys

input = sys.stdin.readline
N = int(input())
calendars = []
for _ in range(N):
    S, E = map(int, input().split())
    calendars.append((S, E))
calendars.sort(key=lambda x : (x[0], -x[1]))

start = calendars[0][0]
end = calendars[0][1]
height = {i:1 for i in range(start, end+1)}
answer = 0
for i in range(1, len(calendars)):
    S, E = calendars[i]
    if S >= start and S <= end + 1:
        if E > end:
            end = E
        for i in range(S, E+1):
            if i in height:
                height[i] += 1
            else:
                height[i] = 1
    else:
        answer += (end - start + 1) * max(height.values())
        start, end = S, E
        height = {i:1 for i in range(start, end+1)}

answer += (end - start + 1) * max(height.values())
print(answer)
