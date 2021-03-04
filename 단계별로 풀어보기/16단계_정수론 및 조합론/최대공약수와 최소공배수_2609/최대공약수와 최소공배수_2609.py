A, B = map(int, input().split())
M = 0
for i in range(1, A + 1):
    if i > A or i > B:
        break
    if A % i == 0 and B % i == 0:
        M = i
print(M)
print(M * (A // M) * (B // M))
