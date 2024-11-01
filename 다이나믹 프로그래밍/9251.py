A = input()
B = input()

LCS = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

for a in range(1, len(A)+1):
    for b in range(1, len(B)+1):
        if A[a-1] == B[b-1]:
            LCS[a][b] = LCS[a-1][b-1] + 1
        else:
            LCS[a][b] = max(LCS[a-1][b], LCS[a][b-1])

print(max(LCS[-1]))