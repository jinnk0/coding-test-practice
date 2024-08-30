def solution(n, lost, reserve):
    lost_list = list(set(lost) - set(reserve))
    reserve_list = list(set(reserve) - set(lost))
    
    for r in sorted(reserve_list):
        if r - 1 in lost_list:
            lost_list.remove(r - 1)
        elif r + 1 in lost_list:
            lost_list.remove(r + 1)

    return n - len(lost_list)
