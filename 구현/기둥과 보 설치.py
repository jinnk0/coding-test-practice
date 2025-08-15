'''
# 프로그래머스 lv.3 기둥과 보 설치

# n x n 크기의 정사각형인 2차원 벽면에 길이가 1인 선분으로 이루어진 기둥과 보를 설치 또는 삭제하는 작업 실행
# 기둥은 좌표 기준 위쪽으로 설치, 보는 좌표 기준 오른쪽으로 설치
# 기둥 설치 조건
    1) 바닥 위에 설치
    2) 보의 한쪽 끝 위에 설치
    3) 다른 기둥 위에 설치
# 보 설치 조건
    1) 한쪽 끝 부분이 기둥 위에 닿게 설치
    2) 양쪽 끝 부분이 다른 보와 연결되게 설치

# 입력 : 벽면의 크기 n, 기둥/보를 설치/삭제하는 작업 순서가 담긴 2차원 배열 build_frame ([x, y, a, b] : x, y는 교차점 좌표, a는 구조물 종류(0은 기둥, 1은 보), b는 작업 종류(0은 삭제, 1은 설치))
# 출력 : 작업이 끝난 후 최종 구조물의 상태를 ([x, y, a]) 가 담긴 2차원 배열 형태로 오름차순 정렬하여 출력

# 1회차 풀이 후기: n과 build_frame의 크기가 크지 않아 전체 검사를 해도 시간이 오래 걸리지 않음 -> 일부만 검사해서 시간을 줄이려고 하면 오히려 오류가 많이 발생하고 오래걸림. 브루트포스 방식이 오히려 효율적
'''
# 현재 구조물 상태(curr_status)가 모든 설치 조건을 만족하는지 확인
def check_validity(n, curr_status):
    for x in range(n + 1):
        for y in range(n + 1):
            # 기둥이 설치되어 있다면
            if curr_status[0][x][y] == 1:
                # 기둥 설치 조건 확인:
                # 1) 바닥 위 (y == 0)
                # 2) 보의 한쪽 끝 위 (curr_status[1][x-1][y] == 1 또는 curr_status[1][x][y] == 1)
                # 3) 다른 기둥 위 (curr_status[0][x][y-1] == 1)
                if not (y == 0 or \
                        (x > 0 and curr_status[1][x-1][y] == 1) or \
                        (curr_status[1][x][y] == 1) or \
                        (y > 0 and curr_status[0][x][y-1] == 1)):
                    return False

            # 보가 설치되어 있다면
            if curr_status[1][x][y] == 1:
                # 보 설치 조건 확인:
                # 1) 한쪽 끝 부분이 기둥 위에 닿게 설치 (curr_status[0][x][y-1] == 1 또는 curr_status[0][x+1][y-1] == 1)
                # 2) 양쪽 끝 부분이 다른 보와 연결되게 설치 (curr_status[1][x-1][y] == 1 and curr_status[1][x+1][y] == 1)
                if not ((y > 0 and curr_status[0][x][y-1] == 1) or \
                        (y > 0 and curr_status[0][x+1][y-1] == 1) or \
                        (x > 0 and curr_status[1][x-1][y] == 1 and curr_status[1][x+1][y] == 1)):
                    return False
    return True

def solution(n, build_frame):
    # 현재 구조물 상태를 저장할 3차원 배열 초기화
    # curr_status[0]은 기둥, curr_status[1]은 보
    # 각 층은 [x][y] 형태로 저장 (1이면 존재, 0이면 없음)
    curr_status = [[[0]*(n+1) for _ in range(n+1)] for _ in range(2)]

    for x, y, a, b in build_frame:
        if b == 1: # 설치
            # 일단 설치 시도
            curr_status[a][x][y] = 1
            # 설치 후 전체 구조물이 유효한지 확인
            if not check_validity(n, curr_status):
                # 유효하지 않다면 다시 되돌리기 (설치 취소)
                curr_status[a][x][y] = 0
        else: # 삭제 
            # 일단 삭제 시도
            curr_status[a][x][y] = 0
            # 삭제 후 전체 구조물이 유효한지 확인
            if not check_validity(n, curr_status):
                # 유효하지 않다면 다시 되돌리기 (삭제 취소)
                curr_status[a][x][y] = 1

    # 모든 작업이 끝난 후 최종 구조물 상태를 [x, y, a] 형태로 변환 및 정렬
    answer = []
    for x in range(n + 1):
        for y in range(n + 1):
            if curr_status[0][x][y] == 1: # 기둥이 있다면
                answer.append([x, y, 0])
            if curr_status[1][x][y] == 1: # 보가 있다면
                answer.append([x, y, 1])
    
    # x좌표 -> y좌표 -> 구조물 종류 순으로 오름차순 정렬
    answer.sort()
    return answer