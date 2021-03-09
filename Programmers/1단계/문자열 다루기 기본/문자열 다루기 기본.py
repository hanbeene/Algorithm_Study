def solution(s):
    if len(s) == 4 or len(s) == 6:
        for i in range(len(s)):
            if not s.isdigit():
                return False
        return True
    else:
        return False



s = "a123"
print(solution(s))