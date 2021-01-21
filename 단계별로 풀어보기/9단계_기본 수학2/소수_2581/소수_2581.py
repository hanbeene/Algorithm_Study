M = int(input())
N = int(input())
L = [True] * 10001
L[0] = False
L[1] = False
for i in range(2,len(L)):
    for j in range(i+i, len(L), i):
        L[j] = False

min = []
for k in range(M,N+1):
    if L[k] == True:
       min.append(k)
if not min:
    print(-1)
else:
    print(sum(min))
    print(min[0])