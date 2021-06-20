def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer += absolutes[i] * -1
    return answer


absolutes = [1, 2, 3]
signs = [False, False, True]
print(solution(absolutes, signs))
