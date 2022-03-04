# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# ...
# ...
# ...

# 코딩테스트에서틑 보통 DFS 보다는 BFS 구현이 조금 더 빠르게 동작하는 정도로 기억하자