'''
# 출처 : 이것이 취업을 위한 코딩테스트다
# 문제 유형 : 그리디
# 입력
    - N : 동전의 개수 (1 <= N <= 1,000)
    - 동전의 화폐 단위를 나타내는 N개의 자연수 (1 <= 각 화폐 단위 <= 1,000,000)
# 출력
    - 주어진 동전들로 만들 수 없는 양의 정수 금액 중 최솟값
'''
N = int(input())
coins = sorted(list(map(int, input().split())))
number = 1
for coin in coins:
    if number < coin:
        print(number)
        break
    else:
        number += coin
            