'''
# 출처 : 이것이 취업을 위한 코딩테스트다
# 문제 유형 : 그리디
# 입력
    - N : 볼링공의 개수 (1 <= N <= 1,000)
    - M : 공의 최대 무게 (1 <= M <= 10)
    - K : 볼링공의 무게 (1 <= K <= M)
# 출력 : 두 사람이 볼링공을 고르는 경우의 수
'''
N, M = map(int, input().split())
K = list(map(int, input().split()))

def getGroupCount(number):
    return number * (number -1 ) // 2

duple = 0
for k in set(K):
    number = K.count(k)
    duple += getGroupCount(number)

print(getGroupCount(N) - duple)