N, K = map(int, input().split())
moneylist = []
cnt = 0
for _ in range(N):
    moneylist.append(int(input()))
for i in range(len(moneylist) - 1, -1, -1):
    if K == 0:
        break
    if moneylist[i] <= K:
        c = K // moneylist[i]
        K = K - (moneylist[i] * c)
        cnt += 1 * c
    elif moneylist[i - 1] <= K < moneylist[i]:
        c = K // moneylist[i - 1]
        K = K - (moneylist[i - 1] * c)
        cnt += 1 * c

print(cnt)
