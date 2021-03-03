import sys

count = int(sys.stdin.readline())
factor = list(map(int, input().split()))
factor.sort()
print(factor[0] * factor[-1])
