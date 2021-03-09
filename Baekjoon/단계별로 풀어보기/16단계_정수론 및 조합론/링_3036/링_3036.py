def gcd(A, B):
    while B > 0:
        A, B = B, A % B
    return A


N = int(input())
number_list = list(map(int, input().split()))
for i in range(1, len(number_list)):
    Q = gcd(number_list[0], number_list[i])
    print(str(number_list[0] // Q) + '/' + str(number_list[i] // Q))
