def solution(n, arr1, arr2):
    sum = ''
    answer = []
    new_arr1 = [format(i, 'b').zfill(n) for i in arr1]
    new_arr2 = [format(i, 'b').zfill(n) for i in arr2]
    for j in range(n):
        for k in range(n):
            if new_arr1[j][k] == '1' or new_arr2[j][k] == '1':
                sum += '#'
            else:
                sum += ' '
        answer.append(sum)
        sum = ''

    return answer


n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))
