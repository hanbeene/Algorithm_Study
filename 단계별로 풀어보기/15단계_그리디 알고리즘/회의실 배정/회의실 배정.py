N = int(input())
time = []
count = []
for _ in range(N):
    time.append(list(map(int, input().split())))
time.sort()
time.sort(key=lambda x: x[1])
count = 1
start, end = time[0]
for i in time[1:]:
    x, y = i
    if end <= x:
        end = y
        count += 1
print(count)
