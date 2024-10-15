'''
# 출처 : 이것이 코딩테스트다
# 문제 유형 : 정렬
# 입력
    - N : 수열에 속해 있는 수의 개수
# 출력 : 수열을 내림차순으로 정렬
'''
N = int(input())
numbers = [int(input()) for _ in range(N)]
print(' '.join(map(str, sorted(numbers, reverse=True))))