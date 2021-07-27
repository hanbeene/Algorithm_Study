count = 0


def DFS(V):
    visited[V] = 1
    global count
    count += 1
    for i in range(1, number + 1):
        if visited[i] == 0 and graph[V][i] == 1:
            DFS(i)


number = int(input())
pairNumber = int(input())
V = 1
graph = [[0] * (number + 1) for i in range(number + 1)]
visited = [0] * (number + 1)

for _ in range(pairNumber):
    x, y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

DFS(V)
print(count - 1)
