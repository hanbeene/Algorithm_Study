L = [True] * 1000001
L[0] = False
L[1] = False
for i in range(2,len(L)):
    for j in range(i+i, len(L), i):
        L[j] = False

M, N = map(int, input().split())
for k in range(M,N+1):
    if L[k] == True:
        print(k)