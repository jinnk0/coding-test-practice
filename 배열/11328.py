N = int(input())
for i in range(N):
    s1, s2 = map(sorted, input().split())
    if s1 == s2:
        print("Possible")
    else:
        print("Impossible")