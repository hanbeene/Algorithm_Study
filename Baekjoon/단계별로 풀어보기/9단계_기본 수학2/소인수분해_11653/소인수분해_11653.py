N = int(input())
i = 2
while N >= i:
    if N % i == 0:
        print(i)
        N = N//i
        if N//i == 1 and N%i == 0:
            print(i)
            break
    else:
        i += 1