n = int(input())  # 원소의 개수
numbers = sorted(list(map(int, input().split())))  # 원소 리스트
sum = int(input())  # 목표 수

start, end = 0, n-1
count = 0

while start < end:
    temp = numbers[start] + numbers[end]
    if temp == sum:
        count += 1
        start += 1
    elif temp > sum:
        end -= 1
    else:
        start += 1

print(count)