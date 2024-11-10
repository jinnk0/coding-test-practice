'''
# 출처 : 백준 1439 문자열 뒤집기
# 문제 유형 : 그리디
# 입력 
    - S : 0과 1로만 이루어진 문자열 (1 <= S의 길이 <= 1,000,000)
# 출력
    - 뒤집기 최소 횟수
'''
S = input()
S_1 = [i for i in S.split('0') if i]
S_0 = [i for i in S.split('1') if i]
print(min(len(S_1), len(S_0)))