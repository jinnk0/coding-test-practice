'''
# 출처 : 백준 2839 설탕배달
# 문제 유형 : 다이나믹 프로그래밍, 그리디
# 입력
    - N : 설탕가게에 배달해야하는 설탕 킬로그램 수 (3 <= N <= 5,000)
# 출력 : 각각 3kg, 5kg 단위의 설탕 봉지가 있을 때 최대한 적은 봉지의 개수
'''
N = int(input())

answer = -1
kg_5 = N // 5
while kg_5 >= 0:
    remainder = N - kg_5 * 5
    if remainder % 3 == 0:
        kg_3 = remainder // 3
        answer = kg_5 + kg_3
        break
    kg_5 -= 1

print(answer)