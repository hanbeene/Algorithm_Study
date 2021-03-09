import math
def solution(n):
    len = int(math.sqrt(n))
    for i in range(len+1):
        if i**2 == n:
            return (i+1)**2
    return -1

print(solution(3))