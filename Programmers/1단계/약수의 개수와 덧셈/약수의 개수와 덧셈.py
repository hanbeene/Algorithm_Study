def solution(left, right):
    answer = []
    for i in range(left, right + 1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count % 2 == 0:
            answer.append(i)
        else:
            answer.append(i * (-1))

    return sum(answer)


print(solution(13, 17))
