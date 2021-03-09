N = int(input())
for i in range(1, N+1):
    M = str(i)
    Q = i
    for j in range(len(M)):
        Q += int(M[j])
    if Q == N:
        print(i)
        break
    if i == N:
        print(0)
        break