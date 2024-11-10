'''
# 출처 : 이것이 취업을 위한 코딩테스트다
# 문제 유형 : 그리디
# 입력
    - S : 여러 개의 숫자로 구성된 하나의 문자열 (1 <= S의 길이 <= 20)
# 출력 
    - 문자열 숫자의 곱하기 혹은 더하기 연산으로 만들어질 수 있는 가장 큰 수
'''
S = list(input())
result = int(S[0])
for i in range(1, len(S)):
    result = max(result * int(S[i]), result + int(S[i]))
print(result)