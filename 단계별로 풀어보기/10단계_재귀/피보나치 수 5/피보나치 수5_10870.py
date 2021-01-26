def Fibo(N):
    if N>= 2:
        return Fibo(N-1) + Fibo(N-2)
    elif N == 1:
        return 1
    elif N == 0:
        return 0


print(Fibo(int(input())))