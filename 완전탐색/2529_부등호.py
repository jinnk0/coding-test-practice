'''
# 출처 : 백준 2529 부등호 (실버1)
# 유형 : 브루트포스, 완전탐색
'''
def count_sequence_length(i, check, cases):
    length = 0
    while i < len(cases) and cases[i] == check:
        length += 1
        i += 1
    return length

k = int(input())
cases = input().split()

max_number = [9]
min_number = [0]

max_check = [True] * 10
min_check = [True] * 10
max_check[max_number[-1]] = False
min_check[min_number[-1]] = False

i = 0
while i < len(cases):
    if cases[i] == '<':
        length = count_sequence_length(i, '<', cases)
        i += length
        max_check[max_number[-1]] = True
        max_number[-1] -= length
        max_check[max_number[-1]] = False
        while length:
            count = 1
            while not max_check[max_number[-1] + count]:
                count += 1
            max_number.append(max_number[-1] + count)
            max_check[max_number[-1]] = False
            length -= 1
    else:
        count = 1
        i += 1
        while not max_check[max_number[-1] - count]:
            count += 1
        max_number.append(max_number[-1] - count)
        max_check[max_number[-1]] = False

i = 0
while i < len(cases):
    if cases[i] == '>':
        length = count_sequence_length(i, '>', cases)
        i += length
        min_check[min_number[-1]] = True
        min_number[-1] += length
        min_check[min_number[-1]] = False
        while length:
            count = 1
            while not min_check[min_number[-1] - count]:
                count += 1
            min_number.append(min_number[-1] - count)
            min_check[min_number[-1]] = False
            length -= 1
    else:
        count = 1
        i += 1
        while not min_check[min_number[-1] + count]:
            count += 1
        min_number.append(min_number[-1] + count)
        min_check[min_number[-1]] = False
        
print(''.join(list(map(str, max_number))))
print(''.join(list(map(str, min_number))))
        

        
    
        