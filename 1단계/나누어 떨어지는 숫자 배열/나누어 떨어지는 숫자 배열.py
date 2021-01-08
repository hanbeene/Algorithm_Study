def solution(arr, divisor):
    newarr = []
    for i in range(len(arr)):
        if arr[i]%divisor == 0:
            newarr.append(arr[i])
    if not newarr:
        newarr.append(-1)
    newarr.sort()
    return newarr

arr = [3, 2, 6]
print(solution(arr,10))