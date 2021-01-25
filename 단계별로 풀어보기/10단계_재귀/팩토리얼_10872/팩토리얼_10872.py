def fec(N):
    return N * fec(N-1) if N > 1 else 1

N = int(input())
print(fec(N))