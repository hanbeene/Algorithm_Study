N = int(input())
time = list(map(int, input().split()))
time.sort()
realanswer = []
for i in range(len(time)):
    answer = 0
    for j in range(i+1):
        answer += time[j]
    realanswer.append(answer)
print(sum(realanswer))