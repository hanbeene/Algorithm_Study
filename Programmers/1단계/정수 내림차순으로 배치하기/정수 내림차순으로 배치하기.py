def solution(n):
    answer = ''
    newn = list(str(n))
    newn.sort(reverse=True)
    return int("".join(newn))
