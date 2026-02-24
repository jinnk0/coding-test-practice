# 현재 캐릭터의 점수 N
N = list(input().strip())

# N을 자릿수를 기준으로 반 나누기
left = N[:len(N)//2]
right = N[len(N)//2:]

# 각 자릿수 합 구하기
def sum_of_digit(digits):
    sum = 0
    for digit in digits:
        sum += int(digit)
    return sum

# 각 자릿수 합이 같으면 "LUCKY" 아니면 "READY"
if sum_of_digit(left) == sum_of_digit(right):
    print("LUCKY")
else:
    print("READY")