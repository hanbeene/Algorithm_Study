def fec(N):
    return N * fec(N - 1) if N > 1 else 1


answer = str(fec(int(input())))
Q = list(answer)
count = 0
for i in range(len(Q) - 1, -1, -1):
    if int(Q[i]) == 0:
        count += 1
    elif int(Q[i]) != 0:
        break

print(count)
