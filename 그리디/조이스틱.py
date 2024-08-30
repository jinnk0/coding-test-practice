def solution(name):
    answer = 0
    for spell in iter(name):
        move = min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)
        answer += move
    move = len(name) - 1
    for i in range(len(name)):
        next_i = i + 1
        while next_i < len(name) and name[next_i] == 'A':
            next_i += 1
        move = min(move, i + 2*(len(name) - next_i), 2*i + (len(name) - next_i))
    answer += move
    return answer
