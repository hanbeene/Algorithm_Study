K = int(input())
Stack = []
for _ in range(K):
    s = int(input())
    if s == 0:
        Stack.pop()
    else:
        Stack.append(s)
print(sum(Stack))