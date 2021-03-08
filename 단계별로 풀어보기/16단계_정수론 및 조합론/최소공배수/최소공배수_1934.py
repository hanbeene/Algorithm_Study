def gcd(A, B):
    while B > 0:
        A, B = B, A % B
    return A


T = int(input())
for _ in range(T):
    A, B = map(int, input().split())
    print(gcd(A, B) * A // gcd(A, B) * B // gcd(A, B))
