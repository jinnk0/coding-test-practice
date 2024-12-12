'''
# 출처 : 백준 15685 드래곤 커브
# 유형 : 구현, 시뮬레이션
# 입력 :
    1. 첫째줄 : 드래곤 커브 개수 N (1  <= N <= 20)
    2. 둘째줄 ~ : N개의 드래곤 커브 정보 x, y, d, g
        - x, y : 드래곤 커브 시작점의 좌표
        - d : 시작 방향 (0: (+1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, +1))
        - g : 드래곤 커브 세대
# 출력 : 드래곤 커브를 그렸을 때 생기는 변의 길이가 1인 정사각형의 개수
'''
import copy
N = int(input())

direction = [(1, 0), (0, -1), (-1, 0), (0, 1)]
points = []
for _ in range(N):
    x, y, d, g = map(int, input().split())
    pointing = []
    points.append((x, y))
    for i in range(g+1):
        if i == 0:
            dx, dy = direction[d]
            x, y = points[-1]
            points.append((x+dx, y+dy))
            pointing.append(d)
        else:
            stack = copy.deepcopy(pointing)
            while stack:
                d = stack.pop()
                dx, dy = direction[(d+1)%4]
                x, y = points[-1]
                points.append((x+dx, y+dy))
                pointing.append((d+1)%4)

x_points = [x for x, y in points]
y_points = [y for x, y in points]

min_x = min(x_points)
max_x = max(x_points)
min_y = min(y_points)
max_y = max(y_points)

points = set(points)

count = 0

for x in range(min_x, max_x):
    for y in range(min_y, max_y):
        if (x, y) in points and (x+1, y) in points and (x, y+1) in points and (x+1, y+1) in points:
            count += 1
print(count)