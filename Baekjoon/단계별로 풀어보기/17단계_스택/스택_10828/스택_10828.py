import sys

N = int(sys.stdin.readline().rstrip())
stack = []
for _ in range(N):
    S = sys.stdin.readline().rstrip().split()
    if S[0] == 'push':
        stack.append(S[1])
    elif S[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif S[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    elif S[0] == 'size':
        print(len(stack))
    elif S[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
