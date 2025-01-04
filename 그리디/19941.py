'''
# 출처 : 백준 19941 햄버거 분배
# 유형 : 그리디
# 입력
    - 첫째줄 : N, K (1 <= N <= 20,000, 1<= K <= 10)
    - 둘째줄 : 햄버거 H, 사람 P 위치
# 출력 : 햄버거를 먹을 수 있는 사람 수 최댓값
'''
N, K = map(int, input().split())
positions = list(input())

count = 0
for i in range(N):
    if positions[i] == 'P':
        for p in range(i-K, i+K+1):
            if p >= 0 and p < N and positions[p] == 'H':
                positions[p] = 'X'
                count += 1
                break

print(count)
