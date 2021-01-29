import sys
N = int(input())
Q = [0] * 10001
for _ in range(N):
    num = int(sys.stdin.readline())
    Q[num] += 1
for i in range(len(Q)):
    if Q[i] != 0:
        for j in range(Q[i]):
            print(i)