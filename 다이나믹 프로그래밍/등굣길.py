'''
# 프로그래머스 lv.3 등굣길
# m x n 격자 모양의 길에서 (1,1)은 집, (m, n)은 학교
# 물에 일부 지역이 잠겼을 때 집에서 학교까지의 최단 경로 개수
# 오른쪽 또는 아래쪽으로만 이동 가능
# 집과 학교는 물에 잠기지 않으며, m과 n이 동시에 1인 경우는 주어지지 않음
# 입력 : m, n (1 <= m, n <= 100), puddles(물에 잠긴 지역 좌표가 담긴 2차원 배열, 길이는 0 이상 10 이하)
# 출력 : 집에서 학교까지의 최단 경로 개수 % 1,000,000,007
'''
def solution(m, n, puddles):
    matrix = [[0] * (m + 1) for _ in range(n + 1)]
    matrix[1][1] = 1
    puddles.append([1, 1])
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if [i, j] in puddles:
                continue
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    return matrix[n][m] % 1_000_000_007
