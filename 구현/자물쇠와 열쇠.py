'''
# 프로그래머스 lv.3 자물쇠와 열쇠

# 자물쇠의 형태는 격자 한 칸의 크기가 1x1인 NxN 크기의 정사각 격자 형태
# 열쇠의 형태는 MxM 크기의 정사각 격자 형태
# 자물쇠와 열쇠에는 홈과 돌기가 존재 (홈은 0 돌기는 1)
# 열쇠는 회전과 이동이 가능
# 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열림
# 입력 : 열쇠와 자물쇠의 홈, 돌기 부분에 대한 배열 (key, lock)
# 출력 : 자물쇠를 열 수 있는 지 여부를 true, false로 반환
'''
# 자물쇠를 열 수 있는 지 검증하는 단계
def is_unlocked(key, lock, x, y):
    n = len(lock)
    m = len(key)
    # 자물쇠와 열쇠 배열을 합했을 때 자물쇠 배열의 모든 원소가 1
    for i in range(n):
        for j in range(n):
            if 0 <= i + x < m and 0 <= j + y < m:
                if lock[i][j] + key[i+x][j+y] != 1:
                    return False
            else:
                if lock[i][j] != 1:
                    return False
    return True

# 열쇠를 오른쪽으로 90도 회전
def rotate(key):
    n = len(key)
    rotated = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n-1-i] = key[i][j]
    return rotated

def solution(key, lock):
    n = len(lock)
    # 90도씩 회전하면서 4방향에 대해 열쇠 위치 이동하며 확인
    for _ in range(4):
        key = rotate(key)
        for x in range(-n+1, n): # 열쇠의 시작 위치 결정 (열쇠의 오른쪽 아래 부분이 자물쇠와 겹치는 경우 ~~ 열쇠의 왼쪽 윗 부분이 자물쇠와 겹치는 경우)
            for y in range(-n+1, n):
                if is_unlocked(key, lock, x, y):
                    return True
    return False # 모두 확인해도 성립하지 않으면 false