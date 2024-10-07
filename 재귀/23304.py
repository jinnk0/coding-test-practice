def validation(S):
    if len(S) == 1:
        return True
    else:
        if S == S[::-1]:
            if len(S) % 2 == 0:
                return validation(S[:len(S)//2]) and validation(S[len(S)//2:])
            else:
                return validation(S[:len(S)//2]) and validation(S[len(S)//2+1:])
        else:
            return False
    
S = input()

if validation(S):
    print("AKARAKA")
else:
    print("IPSELENTI")
