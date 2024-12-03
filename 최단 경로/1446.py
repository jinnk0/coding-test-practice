'''
# 출처 : 백준 1446 지름길
# 문제 유형 : 최단 경로, 다익스트라, DP
# 입력
    - N : 지름길의 개수 (1 <= N <= 12)
    - D : 고속도로의 길이 (1 <= D <= 10,000)
    - 지름길 출발점, 지름길 도착점, 지름길 길이 (x N개)
# 출력 : 목적지까지 가기 위해 운전해야 하는 거리의 최소값
'''
N, D = map(int, input().split())
shortcuts = []
for _ in range(N):
    start, end, length = map(int, input().split())
    if end <= D:
        shortcuts.append((start, end, length))

distance = [i for i in range(D + 1)]

for i in range(D + 1):
    if i > 0:
        distance[i] = min(distance[i], distance[i - 1] + 1)

    for start, end, length in shortcuts:
        if i == start and distance[i] + length < distance[end]:
            distance[end] = distance[i] + length

print(distance[D])