def solution(lottos, win_nums):
    counter = 0
    answer = []
    dic = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    for lotto in lottos:
        if win_nums.count(lotto) > 0:
            counter += 1
    answer.append(dic[counter + lottos.count(0)])
    answer.append(dic[counter])
    return answer


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))
