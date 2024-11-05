'''
# 출처 : 이것이 취업을 위한 코딩테스트다
# 문제 유형 : 그래프 이론
# 입력
    N M
    (0 or 1) a b (M개)
    - N : 학생에게 부여되는 번호(0~N, 총 N+1개)
    - M : 입력으로 주어지는 연산의 개수
    - 0 : a번 학생이 속한 팀과 b번 학생이 속한 팀을 합치는 연산
    - 1 : a번 학생과 b번 학생이 같은 팀에 속해 있는지 확인 (출력값 발생)
# 출력
    YES or NO(같은 팀 여부 확인)
'''
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
N, M = map(int, input().split())
parent = [0] * (N + 1)

for i in range(N+1):
    parent[i] = i

for i in range(M):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union_parent(parent, a, b)
    elif oper == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')