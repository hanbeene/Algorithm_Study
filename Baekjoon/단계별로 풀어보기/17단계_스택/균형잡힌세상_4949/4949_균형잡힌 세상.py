while True:
    a = input()
    if a == '.':
        break
    stack = []
    answer = 'yes'
    for i in a:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                answer = 'no'
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                answer = 'no'
                break
    if len(stack) == 0:
        print(answer)
    else:
        print('no')
