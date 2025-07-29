'''
# 프로그래머스 lv.2 문자열 압축

# 문자열에서 같은 값이 연속으로 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 압축
# 문자가 반복되지 않아 한번만 나타난 경우 1은 생략
# 반복되는 문자를 1개 단위, 2개 단위, .. n개 단위로 잘라 압축할 때 가장 짧은 것의 길이 구하기
# 문자열을 자를 때 앞에서부터 순서대로 정해진 단위만큼 자름

# 입력 : 문자열 s (s의 길이는 1 이상 1,000 이하, 알파벳 소문자로만 구성)
# 출력 : 가장 짧은 압축된 문자열의 길이
'''
def solution(s):
    answer = len(s)
    # 문자열 단위를 1부터 문자열의 길이 / 2까지 반복하며 가장 짧은 문자열의 길이(answer) 저장 (1000 x 500 -> 최악의 경우 5만번)
    for size in range(1, len(s)//2 + 1):
        # 문자열 앞에서 문자열 분할 단위 기준으로 건너뛰며 확인 (이전 문자열 단위 저장 prev)
        prev_substr = s[:size]
        count = 1
        compressed = ""
        for j in range(size, len(s), size):
            curr_substr = s[j:j+size]
            # 이전 문자열 단위와 비교하여 같은 경우 count + 1
            if prev_substr == curr_substr:
                count += 1
            else: # 다른 경우 압축된 문자열에 count + prev를 추가하고 prev 현재 문자 단위로 변경
                compressed += f"{count}{prev_substr}" if count > 1 else prev_substr
                prev_substr = curr_substr
                count = 1
        compressed += f"{count}{prev_substr}" if count > 1 else prev_substr
        answer = min(answer, len(compressed))
    return answer