'''
# 출처 : 백준 1461 도서관
# 문제 유형 : 그리디, 정렬
# 입력 
    1. 첫째 줄 : 책의 개수 N (1 <= N <= 50)
    2. 첫째 줄 : 한 번에 들 수 있는 책의 개수 M (1 <= M <= 50)
    3. 둘째 줄 : N개의 책의 위치 (0이 아니고 절대값이 10,000보다 작거나 같은 정수)
# 출력 
    1. 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수
'''
N, M = map(int, input().split())
positions = list(map(int, input().split()))
plus_pos = []
minus_pos = []
for pos in positions:
    if pos > 0:
        plus_pos.append(pos)
    else:
        minus_pos.append(pos)

minus_pos = sorted(list(map(abs, minus_pos)), reverse=True)
plus_pos = sorted(plus_pos, reverse=True)

select_pos = minus_pos[::M]
select_pos.extend(plus_pos[::M])

answer = max(select_pos)
select_pos.remove(answer)

for pos in select_pos:
    answer += pos * 2

print(answer)
