'''
# 출처 : 프로그래머스 Lv.2 전화번호 목록
# 유형 : 해시
'''
def solution(phone_book):
    hash = {}
    for number in phone_book:
        hash[number] = 1
    for number in phone_book:
        prefix = ""
        for num in number:
            prefix += num
            if prefix != number and prefix in hash:
                return False
    return True
