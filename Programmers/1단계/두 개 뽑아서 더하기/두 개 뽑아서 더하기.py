def solution(numbers):
    newarr = []
    for i in range(len(numbers)):
        for j in range(i):
            if numbers[i] + numbers[j] not in newarr:
                newarr.append(numbers[i]+numbers[j])
    newarr.sort()
    return newarr

arr = [5,0,7,2]
print(solution(arr))