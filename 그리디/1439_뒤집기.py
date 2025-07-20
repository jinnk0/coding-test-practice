s = input() # 0과 1로만 이루어진 문자열
s0 = [i for i in s.split('1') if i] # 모두 1로 만들기 위해 뒤집어야 하는 단위 문자열
s1 = [i for i in s.split('0') if i] # 모두 0으로 만들기 위해 뒤집어야 하는 단위 문자열

print(min(len(s0), len(s1))) # 단위 문자열의 개수가 더 적은 쪽을 출력
