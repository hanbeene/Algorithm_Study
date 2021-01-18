x = int(input())
seq = 0
i = 0
while seq < x:
    i += 1
    seq += i

if i%2 == 1:
    print(str(seq-x+1)+'/'+str(i - (seq-x)))
else:
    print(str(i-(seq-x))+'/'+ str(seq-x+1))