def solution(word):
    def next_alpha(alpha):
        words = ["A", "E", "I", "O", "U"]
        for i in range(len(words)):
            if alpha == "U":
                return ""
            if words[i] == alpha:
                return words[i+1]
    def search(current, target):
        cnt = 1
        while (current != target):
            if len(current) < 5:
                current += "A"
            else:
                current[-1] = next_alpha(current[-1])
                while current[-1] == "":
                    current = current[:-1]
                    current[-1] = next_alpha(current[-1])
            cnt += 1
        return cnt
    return search(['A'], list(word))