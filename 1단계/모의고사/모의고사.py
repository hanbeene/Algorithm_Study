def solution(answer):
    number1 = [1, 2, 3, 4, 5]
    number2 = [2, 1, 2, 3, 2, 4, 2, 5]
    number3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]
    answers = []
    for i in range(len(answer)):
        if answer[i] == number1[i % 5]:
            count[0] += 1
        if answer[i] == number2[i % 8]:
            count[1] += 1
        if answer[i] == number3[i % 10]:
            count[2] += 1
    for i in range(3):
        if count[i] == max(count):
            answers.append(i+1)
    return answers


answer = [1, 2, 3, 4, 5]
print(solution(answer))
