'''
# 출처 : 이것이 취업을 위한 코딩테스트다
# 문제 유형 : 그리디
# 입력
    - N : 모험가의 수 (1 <= N <= 100,000)
    - 각 모험가의 공포도 값 N 이하의 N개의 자연수
# 출력
    - 여행을 떠날 수 있는 그룹 수의 최댓값
'''
N = int(input())
members = sorted(list(map(int, input().split())), reverse=True)
count = 0
while members:
    member = members.pop()
    if member == 1:
        count += 1
    elif member <= len(members):
        for _ in range(member-1):
            members.pop()
            count += 1

print(count)