def solution(x, n):
    answer = []
    count = 1
    for i in range(n):
        answer.append(x*count)
        count +=1
    return answer

x = -4
n = 2
print(solution(x,n))