import sys
from collections import Counter
N = int(input())
Q = []
for _ in range(N):
    Q.append(int(sys.stdin.readline()))
# 산술평균
print(round(sum(Q)/N))
# 중앙값
Q.sort()
print(Q[N//2])
# 최빈값
K = Counter(Q).most_common()
if len(Q) > 1:
    if K[0][1] == K[1][1]:
        print(K[1][0])
    else:
        print(K[0][0])
else:
    print(K[0][0])
# 범위
print(Q[-1] - Q[0])