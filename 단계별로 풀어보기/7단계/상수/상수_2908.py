S = input().split()
A = list(map(int, S[0]))
A.reverse()
B = list(map(int, S[1]))
B.reverse()
NewA = ''
NewB = ''
for i in range(3):
    NewA += str(A[i])
    NewB += str(B[i])
if int(NewA) > int(NewB):
    print(NewA)
else:
    print(NewB)