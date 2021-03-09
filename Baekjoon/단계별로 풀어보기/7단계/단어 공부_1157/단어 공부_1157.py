S = input().upper()
Count = [0]*26
jj = 0
for i in str(S):
    Count[ord(i)-65] = Count[ord(i)-65]+1
maxnum = Count.index(max(Count))
maxCount = Count[Count.index(max(Count))]
for j in range(len(Count)):
    if Count[j] == maxCount:
        jj += 1
if jj >= 2:
    print('?')
else:
    print(chr(maxnum+65))