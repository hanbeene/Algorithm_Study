N = int(input())
numbers = sorted(list(map(int, input().split())))

left, right = 0, N - 1
answer = []
min = abs(numbers[left] + numbers[right])
cleft = left
cright = right

while left < right:
    temp = numbers[left] + numbers[right]
    if abs(temp) < min:
        cleft = left
        cright = right
        min = abs(temp)
        if min == 0:
            break
    if temp > 0:
        right -= 1
    else:
        left += 1

print(numbers[cleft], numbers[cright])
