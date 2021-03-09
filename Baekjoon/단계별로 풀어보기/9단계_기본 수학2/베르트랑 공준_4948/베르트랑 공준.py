sosulist = [True] * ((123457 * 2)+1)
sosulist[0] = False
sosulist[1] = False

for i in range(2, len(sosulist)):
    for j in range(i+i, len(sosulist), i):
        sosulist[j] = False
while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for k in range(n+1, (n*2)+1):
        if sosulist[k] == True:
            count += 1
    print(count)