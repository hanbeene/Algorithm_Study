def fec(A):
    return A * fec(A - 1) if A > 1 else 1


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(int(fec(B) / (fec(B - A) * fec(A))))
