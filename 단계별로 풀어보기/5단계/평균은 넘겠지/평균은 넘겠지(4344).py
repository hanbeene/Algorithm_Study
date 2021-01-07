C = int(input())
for i in range(C):
    sum = 0
    count = 0
    a = list(map(int, input().split()))
    for j in range(1, len(a)):
        sum += a[j]
    average = sum/(len(a)-1)
    for k in range(1, len(a)):
        if a[k] > average: count += 1
    print('%.3f'%(count/(len(a)-1) * 100)+'%')