def fec(A):
    return A*fec(A-1) if A > 1 else 1

N, K = map(int, input().split())
print(int(fec(N)/(fec(N-K) * fec(K))))