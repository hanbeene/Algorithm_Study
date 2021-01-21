N = int(input())
L = [True] * 1001
L[0] = False
L[1] = False
for i in range(2,len(L)):
    for j in range(i+i, len(L), i):
        L[j] = False

count = 0
Q = list(map(int, input().split()))
for k in range(len(Q)):
    if L[Q[k]] == True:
        count += 1
print(count)