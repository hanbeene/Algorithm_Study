T = int(input())
for _ in range(T):
    stack = list(str((input())))
    check = 0
    check2 = 0
    for i in range(len(stack) - 1, -1, -1):
        if stack[i] == ')':
            check += 1
        else:
            check -= 1
        if check < 0:
            check2 += 1
            print('NO')
            break
    if check == 0:
        print('YES')
    elif check2 != 1 and check != 0:
        print('NO')
