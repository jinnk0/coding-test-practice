'''
# 출처 : 이것이 코딩테스트다
# 문제 유형 : 정렬
# 입력
    - N : 학생 수(1 <= N <= 100,000)
    - A : 학생 이름
    - B : 성적 정보
# 출력 : 학생 이름(성적 오름차순)
'''
N = int(input())
students = []
for _ in range(N):
    A, B = input().split()
    students.append((A, int(B)))
students.sort(key=lambda x:x[1])
result = ''
for student in students:
    result += ' ' + student[0]
print(result)