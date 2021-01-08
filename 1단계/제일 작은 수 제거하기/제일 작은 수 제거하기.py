def solution(arr):
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] < min:
            min = arr[i]
    del arr[arr.index(min)]
    if not arr:
        arr.append(-1)
    return arr

arr = [10]
print(solution(arr))