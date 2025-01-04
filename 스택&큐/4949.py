'''
# 출처 : 백준 4949 균형잡힌 세상
# 난이도 : 실버4
# 유형 : 스택
# 입력 : 온점(".")으로 끝나는 영문 알파벳, 소괄호("()"), 대괄호("[]")로 이루어진 100글자 이내의 문자열
# 출력 : 문자열의 괄호가 균형이면 "yes", 아니면 "no"
'''
pair = {"(":")", "[":"]"}
sentence = input()
while sentence != ".":
    stack = []
    balance = True
    for s in sentence:
        if s in pair.keys():
            stack.append(s)
        elif s in pair.values():
            if stack and pair[stack[-1]] == s:
                stack.pop()
            else:
                balance = False
                break
    if balance and not stack:
        print("yes")
    else:
        print("no")
    
    sentence = input()