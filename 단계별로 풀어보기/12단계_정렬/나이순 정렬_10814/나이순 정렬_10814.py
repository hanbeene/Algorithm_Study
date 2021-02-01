N = int(input())
Q = []
for _ in range(N):
    age, name = input().split()
    Q.append((int(age),name))
Q.sort(key=lambda x:x[0])
for i in range(len(Q)):
    newage = Q[i][0]
    newname = Q[i][1]
    print(newage,newname)