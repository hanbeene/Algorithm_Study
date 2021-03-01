N = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

min_price = city[0]
answer = 0
for i in range(len(road)):
    if min_price > city[i]:
        min_price = city[i]
    answer += min_price * road[i]

print(answer)
