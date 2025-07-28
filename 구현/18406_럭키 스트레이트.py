'''
# 백준 브론즈2 18406 럭키 스트레이트

# 럭키 스트레이트라는 기술은 게임 내에서 점수가 특정 조건을 만족해야 사용 가능
# 조건 : 점수 N의 자릿수를 기준으로 반으로 나누어 왼쪽 부분의 각 자릿수 합과 오른쪽 부분의 각 자릿수 합을 더한 값이 동일한 상황
# 현재 점수 N이 주어질 때 럭키 스트레이르틑 사용할 수 있는 상태인지 아닌지를 알려주는 프로그램 작성

# 입력 : 현재 점수 N (10 <= N <= 99,999,999, N은 정수이고, N의 자릿수는 항상 짝수)
# 출력 : 럭키 스트레이트를 사용할 수 있다면 "LUCKY", 없다면 "READY" 출력
'''
# 현재 점수 N 입력 받기 (문자열로)
N = input()
# N의 길이를 기준으로 왼쪽/오른쪽 분할
left = N[:len(N)//2]
right = N[len(N)//2:]
# 각 자릿수의 합을 계산하는 함수 
def sum_of_digits(number):
    sum = 0
    while(number != 0):
        sum += (number % 10)
        number //= 10
    return sum

# 왼쪽, 오른쪽의 자릿수 합이 같다면 "LUCKY" 출력
if sum_of_digits(int(left)) == sum_of_digits(int(right)):
    print("LUCKY")
# 다르면 "READY" 출력
else:
    print("READY")