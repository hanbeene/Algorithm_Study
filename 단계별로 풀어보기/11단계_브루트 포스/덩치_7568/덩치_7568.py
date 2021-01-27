N = int(input())
Body = []
countlist = []
for _ in range(N):
    Body.append(list(map(int,input().split())))
for i in range(N):
    count = 1
    for j in range(N):
        if Body[i][0] < Body[j][0] and Body[i][1] < Body[j][1]:
            count += 1
    countlist.append(count)
for k in range(len(countlist)):
    print(countlist[k],end=' ')