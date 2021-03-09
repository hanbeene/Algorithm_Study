A, B, V = map(int, input().split())
X = int((V-B)/(A-B))
if ((V-B) % (A - B)) == 0:
    print(X)
else:
    print(X+1)