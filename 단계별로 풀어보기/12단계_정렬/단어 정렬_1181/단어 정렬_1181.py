N = int(input())
Q = []
for _ in range(N):
    word = input()
    wordlen = len(word)
    Q.append((word,wordlen))
newQ = list(set(Q))
newQ.sort(key=lambda x:(x[1],x[0]))
for i in range(len(newQ)):
    so = newQ[i]
    print(so[0])