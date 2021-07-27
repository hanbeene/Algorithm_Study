from collections import deque

def bfs(V):
    # 시작 노드를 큐에 넣음
    queue = deque([V])
    # 시작 노드 방문 처리 ( DFS에 의해 모두 1로 변한 상태이므로 0으로 바꿈)
    visited[V] = 0
    # 큐가 있는 동안
    while queue:
        # 큐에서 하나를 꺼냄
        V = queue.popleft()
        print(V, end=' ')
        # 꺼낸 큐에서 방문할 수 있는 모든 정점을 탐색
        for i in range(1, N+1):
            # 만약 방문하지 않았고, 방문 할 수 있다면 큐에 저장
            if visited[i] == 1 and graph[V][i] == 1:
                queue.append(i)
                visited[i] = 0

def dfs(V):
    # 현재 노드를 방문 처리
    visited[V] = 1
    print(V, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range(1, N + 1):
        # 방문하지 않았고, 현재에서 갈 수 있는곳(1)이 있다면 방문
        if visited[i] == 0 and graph[V][i] == 1:
            dfs(i)


# 정점의 개수 N, 간선의 개수 M, 탐색을 시작할 정점의 번호 V
N, M, V = map(int, input().split())
# 1번부터 시작하기 때문에 인덱스를 맞춰주기 위해 N+1을 해줌
graph = [[0] * (N + 1) for i in range(N + 1)]
visited = [0] * (N + 1)
for i in range(M):
    x, y = map(int, input().split())
    # 양방향 간선이기 때문에 만약
    # ex) 1, 2 라면 1에서 2를 갈 수 도 있고, 2에서 1을 갈 수도 있기 때문
    graph[x][y] = 1
    graph[y][x] = 1

dfs(V)
print()
bfs(V)
