'''
# 출처 : 백준 1541 잃어버린 괄호
# 문제 유형 : 그리디
# 입력 : 숫자와 +, -로만 이루어진 식, 
    - 시작과 끝은 숫자
    - 두 개 이상의 연속된 연산자 x
    - 숫자는 최대 다섯자리 수
    - 숫자는 0으로 시작 가능
    - 식의 길이는 50보다 작거나 같음
# 출력 : 해당 식에 괄호를 적절히 쳐서 만들 수 있는 최소값
'''
S = input()

formulas = S.split('-')
numbers = []

for formula in formulas:
    num = ""
    number = 0
    for i in range(len(formula)):
        if formula[i] == '+':
            number += int(num)
            num = ""
        else:
            num += formula[i]
    number += int(num)
    numbers.append(number)

answer = numbers[0]
for i in range(1, len(numbers)):
    answer -= numbers[i]
print(answer)
        

