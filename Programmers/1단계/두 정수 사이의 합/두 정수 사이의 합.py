def solution(a, b):
    sum = 0
    if a<b:
        for i in range(a, b+1):
            sum += a
            a +=1
        return sum
    else:
        for i in range(b, a+1):
            sum += b
            b += 1
        return sum

print(solution(5, 3))