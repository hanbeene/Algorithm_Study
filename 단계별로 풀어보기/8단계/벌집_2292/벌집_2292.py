N = int(input())
Count = 1
Room = 1
while N > Room:
    if N == 1:
        print(1)
    else:
        Room += Count * 6
        Count += 1
print(Count)