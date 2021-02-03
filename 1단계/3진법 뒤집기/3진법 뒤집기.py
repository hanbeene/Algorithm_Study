def solution(n):
    threelist = []
    while n >= 3:
        threelist.append(n%3)
        n = n//3
    threelist.append(n)
    count = 0
    sum = 0
    print(threelist)
    for i in range(len(threelist)-1, -1, -1):
        sum += threelist[i] * (3**count)
        count += 1
    return sum

n = 45
print(solution(n))