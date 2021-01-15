N = int(input())
count = 0
for i in range(N):
    S = input()
    for j in range(len(S)):
        num = S[j:].count(S[j])
        if S[j] in S[j + num:]:
            count -= 1
            break
    count += 1
print(count)
