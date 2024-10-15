'''
# 출처 : 이것이 코딩테스트다
# 문제 유형 : 정렬
# 입력
    - N, K : 배열 크기(원소 개수), 바꿔치기 연산 수 (1 <= N <= 100,000, 0 <= K <= N)
    - 배열 A (1 <= 배열의 원소 < 10,000,000)
    - 배열 B (1 <= 배열의 원소 < 10,000,000)
# 출력 : 배열 A의 모든 원소의 합의 최대값
'''
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for _ in range(K):
    maxB = max(B)
    minA = min(A)
    if minA < maxB:
        A[A.index(minA)] = maxB
        B[B.index(maxB)] = minA
print(sum(A))

