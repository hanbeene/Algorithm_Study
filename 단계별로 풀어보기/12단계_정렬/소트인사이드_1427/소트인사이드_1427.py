N = str(input())
Q = []
for i in range(len(N)):
    Q.append(N[i])
Q.sort(reverse=1)
Result = ''
for j in range(len(Q)):
    Result += str(Q[j])
print(int(Result))