import sys
N = sys.stdin.readline()
Q = []
for _ in range(int(N)):
    Q.append(list(map(int, sys.stdin.readline().split())))
Q.sort(key=lambda x: (x[1],x[0]))
for i in range(len(Q)):
    print(Q[i][0], Q[i][1])