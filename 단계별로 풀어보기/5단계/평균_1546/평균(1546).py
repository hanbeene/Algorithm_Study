N = int(input())
Score = list(map(int, input().split()))
M = max(Score)
NewScore = 0
for i in range(N):
    NewScore += Score[i]/M*100
print(NewScore/N)