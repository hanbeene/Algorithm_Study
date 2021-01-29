import sys
N = int(sys.stdin.readline())
Q = []
for _ in range(N):
    Q.append(list(map(int, sys.stdin.readline().split())))
Q.sort(key=lambda x: (x[0], x[1]))
for i in range(len(Q)):
    print(Q[i][0],Q[i][1])