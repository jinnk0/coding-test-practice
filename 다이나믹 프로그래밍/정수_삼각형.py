def solution(triangle):
    for h in range(1, len(triangle)):
        for w in range(len(triangle[h])):
            if h > 1 and w != 0 and w != len(triangle[h]) - 1:
                triangle[h][w] += max(triangle[h-1][w-1], triangle[h-1][w])
            else:
                if w == 0:
                    triangle[h][w] += triangle[h-1][0]
                else:
                    triangle[h][w] += triangle[h-1][-1]
    return max(triangle[-1])
