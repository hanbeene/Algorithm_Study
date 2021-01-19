T = int(input())
for i in range(T):
    H, W, N = map(int,input().split())
    if N - (H*(N//H)) == 0:
        print(str(H) + str(((N//H))).zfill(2))
    else:
        print(str(N-(H*(N//H))) + str(((N//H)+1)).zfill(2))
