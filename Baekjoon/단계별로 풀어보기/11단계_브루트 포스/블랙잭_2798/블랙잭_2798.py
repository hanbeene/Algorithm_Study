N, M = map(int, input().split())
card = list(map(int, input().split()))
sum = card[0]+card[1]
for i in range(0,len(card)-2):
    for j in range(i+1,len(card)-1):
        for k in range(j+1, len(card)):
            if sum < card[i] + card[j] + card[k] <= M:
                sum = card[i] + card[j] + card[k]
print(sum)