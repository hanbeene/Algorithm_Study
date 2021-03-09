def solution(arr):
    newarr = []
    newarr.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            newarr.append(arr[i])
    return newarr


arr = [4,4,4,3,3]
print(solution(arr))
