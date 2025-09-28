'''
# 프로그래머스 lv.3 외벽 점검
'''
from itertools import permutations

def solution(n, weak, dist):
    w = len(weak)
    # 취약점 배열 확장
    weak = weak + [w + n for w in weak]

    # 투입할 친구 수 1명부터 len(dist)명까지 시도
    for num_friends in range(1, len(dist) + 1):
        # dist 배열에서 num_friends명을 뽑아 만들 수 있는 순열 모두 확인
        for friends_order in permutations(dist, num_friends):
            # 취약점 점검을 시작할 위치를 바꿔가며 모두 시도
            for start in range(w):
                # 처음으로 투입된 친구가 시작한 위치에서 커버할 수 있는 끝 위치
                coverage_end = weak[start] + friends_order[0]
                friend_idx = 0 # 현재 투입된 친구의 인덱스

                # 시작한 위치에서 + (w-1)까지의 취약점을 모두 확인
                covered = True
                i = start
                while i < start + w:
                    if weak[i] <= coverage_end: # 투입된 친구가 커버할 수 있는 취약점
                        i += 1
                    else: # 투입된 친구가 커버할 수 없는 취약점
                        friend_idx += 1 # 다음 친구 투입
                        if friend_idx >= num_friends: # 더 투입할 수 있는 친구가 없음
                            covered = False
                            break
                        # 다음 투입된 친구가 커버할 수 있는 끝 위치 갱신
                        coverage_end = weak[i] + friends_order[friend_idx]

                if covered: # 현재 투입한 친구 수만으로 모든 취약점을 커버할 수 있을 경우
                    return num_friends 

    return -1