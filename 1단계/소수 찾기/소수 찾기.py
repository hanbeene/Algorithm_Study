def solution(n):
    table = [True] * (n+1)
    max_length = int(n ** 0.5)
    for i in range(2, max_length+1):
        if table[i] == True:
            for j in range(i*2, n+1, i):
                table[j] = False
    return len([i for i in range(2, n+1) if table[i] == True])

print(solution(10))