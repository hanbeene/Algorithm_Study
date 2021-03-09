N = int(input())
count = 0
while N >= 0:
    if N % 5 == 0:
        print(N // 5 + count)
        break
    N = N - 3
    count += 1
else:
    print(-1)
