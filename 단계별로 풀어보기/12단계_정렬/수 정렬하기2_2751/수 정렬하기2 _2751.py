import sys
N = int(input())
Q = []
for _ in range(N):
    Q.append(int(sys.stdin.readline()))
for i in sorted(Q):
    sys.stdout.write(str(i)+'\n')