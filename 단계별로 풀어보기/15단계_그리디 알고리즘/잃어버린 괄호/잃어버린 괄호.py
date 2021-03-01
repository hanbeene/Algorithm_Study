s = input().split('-')
num = []
for i in s:
    cnt = 0
    a = i.split('+')
    for j in a:
        cnt += int(j)
    num.append(cnt)
answer = num[0]
for k in range(1, len(num)):
    answer -= num[k]
print(answer)
