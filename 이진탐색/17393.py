'''
# 출처 : 백준 17393 다이나믹 롤러
# 유형 : 이진 탐색
# 입력
    1. 첫째줄 : 통로의 길이 자연수 N (1 <= N <= 500,000)
    2. 둘째줄 : 잉크 지수 A, N개의 정수 (1 <= A <= 10^18)
    3. 셋째줄 : 점도 지수 B, N개의 정수 (1 <= B <= 10^18, A > B)
# 출력 : 각 칸에서 칠할 수 있는 최대 칸수
'''
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

answer = []
for i in range(N):
    start = i+1
    end = N-1
    while (start <= end):
        mid = (start + end) // 2
        if B[mid] <= A[i]:
            start = mid + 1
        else:
            end = mid -1
    answer.append(start - i-1)

print(*answer)