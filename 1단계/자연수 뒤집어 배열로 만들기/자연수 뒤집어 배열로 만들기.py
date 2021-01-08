def solution(n):
    newn = str(n)
    list = []
    for i in range(len(newn)):
        list.append(int(newn[i]))
    list.reverse()
    return list
print(solution(12345))