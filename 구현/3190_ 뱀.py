'''
# 백준 골드4 3190 뱀

# 뱀이 나와서 사과를 먹으면 뱀 길이가 늘어나고, 벽 또는 자기자신의 몸과 부딪히면 게임 종료
# 게임은 NxN 정사각 보드 위에서 진행
# 보드의 상하좌우 끝에는 벽이 존재하고, 사과가 놓여져있는 칸 존재
# 게임을 시작할 때 뱀은 맨 위 좌측에서 시작, 향하는 방향은 오른쪽 뱀의 길이는 1
# 뱀 이동 규칙
    1. 먼저 몸길이를 늘려 머리를 다음칸으로 이동
    2. 벽이나 자기자신의 몸과 부딪히면 (다음칸이 벽 또는 자기자신으로 채워져있을 경우) 게임 종료
    3. 이동한 칸에 사과가 있다면 그 칸에 있던 사과는 없어지고 꼬리는 움직이지 않음 (몸길이 1 증가)
    4. 이동한 칸에 사과가 없다면 몸길이를 줄여서 꼬리가 위치한 칸을 비움 (몸길이 변하지 않음)
# 입력 : 보드의 크기 N, 사과의 개수 K, 사과의 위치(행 열), 뱀의 방향 변환 횟수 L, 뱀의 방향 변환 정보(X초 후에 C:L(왼쪽), D(오르쪽)으로 90도 회전)
# 출력 : 게임이 종료되는 시간
'''
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())
apples = set()
for _ in range(K):
    a, b = map(int, input().split())
    apples.add((a, b))
L = int(input())
routes = {}
for _ in range(L):
    X, C = input().strip().split()
    routes[int(X)] = C

# 뱀의 이동 경로 시뮬레이션
curr = 0 # 게임 시간
snakes_pos = set() # 뱀의 현재 차지하고 있는 위치 (충돌 체크)
snakes_pos.add((1, 1))
snakes = deque([(1, 1)]) # 뱀의 머리부터 꼬리까지 위치 (순서대로)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 회전 시 방향
direct = 0 # 시작할 때 향하는 방향(오른쪽)
game_running = True

while game_running:
    curr += 1

    # 먼저 몸길이를 늘려 머리를 다음칸으로 이동
    head = (snakes[0][0] + directions[direct][0], snakes[0][1] + directions[direct][1])
    if not (0 < head[0] <= N and 0 < head[1] <= N) or head in snakes_pos: # 벽이나 자기자신의 몸과 부딪힌 경우
        game_running = False # 게임 종료
        continue
    # 이동한 칸에 사과가 있는지 확인
    if head in apples: # 이동한 칸에 사과가 있다면
        apples.remove(head) # 그 칸에 있던 사과 제거
        # 꼬리는 움직이지 않고 머리칸만큼 뱀 길이 증가
        snakes.appendleft(head)
        snakes_pos.add(head)
    else: # 이동한 칸에 사과가 없다면
        # 꼬리가 위치한 칸을 비움
        snakes.appendleft(head)
        snakes_pos.add(head)
        tail = snakes.pop()
        snakes_pos.remove(tail)
    
    # x초 후에 방향 전환
    if curr in routes: 
        c = routes[curr]
        if c == 'D': # 오른쪽으로 회전
            direct = (direct + 1) % 4
        else: # 왼쪽으로 회전
            direct = (direct + 3) % 4

print(curr)
