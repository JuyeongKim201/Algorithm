# 문제: DFS와 BFS (실버 2)
'''
무방향 그래프에 대한 DFS, BFS 구현 문제

<시도해볼 것>
- 그래프를 1) 인접 리스트법으로 표현 2) 인접행렬법으로 표현
- DFS를 1) 스택으로 표현 2) 재귀함수로 표현 
'''
from collections import deque

# ------- 그래프 표현 -------
# 그래프 표현 - 1) 인접 리스트
def AdjacencyList(V, E):
    # 리스트 구조 세팅
    graph = {} 
    for i in range(1, V+1):
        graph[i] = []

    # 연결 관계 채우기
    for i in range(E):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)
    
    # (문제 조건) 오름차순 출력을 위해 인접 노드 정렬하기
    for key in graph:
        graph[key].sort()
    
    return graph

# 그래프 표현 - 2) 인접 행렬
def AdjacencyArray(V, E):
    # 행렬 구조 세팅
    graph = []
    for i in range(V+1): # 정점 번호가 1부터 시작하는 문제 특성상, 편의를 위해 0행과 0열은 비워둠
        graph.append(list(0 for i in range(V+1))) 

    # 연결 관계 채우기
    for i in range(E):
        x, y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1

    return graph


# ------- DFS, BFS 구현 (인접 리스트 기준)-------
# DFS 구현(1): 스택 활용
def DFS_stack(graph, start):
    # 방문 목록 만들기
    visited = []
    # 시작 노드를 스택에 넣어준다. 
    stack = [start]
    
    # 스택이 비어있지 않는 동안
    while stack:
        node = stack.pop() # 스택의 맨 위 노드를 꺼낸다.

        if node not in visited: # 아직 방문하지 않았다면,
            print(node, end=' ') # 출력
            visited.append(node) # 방문 처리
            stack.extend(sorted(graph[node], reverse=True)) # 인접 노드를 스택에 넣기
            # 오름차순으로 출력하라는 문제 특성상, 스택에는 역으로 넣어줘야 한다.

    return


# DFS 구현(2): 재귀 함수 활용
def DFS_recursion(graph, node, visited):
    print(node, end=' ') # 출력
    visited.append(node) # 방문 처리

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[node]:
        if i not in visited: # 아직 방문하지 않았다면
            DFS_recursion(graph, i, visited)



# BFS 구현
def BFS(graph, start):
    # 방문 목록 만들기
    visited = []
    # 시작 노드를 큐에 넣어준다.
    que = deque([start]) 

    # 큐가 비어있지 않는 동안
    while que:
        node = que.popleft() # 큐에서 맨 아래 노드를 꺼낸다.
        if node not in visited: # 아직 방문하지 않았다면,
            print(node, end=' ') # 출력
            visited.append(node) # 방문 처리

            for i in graph[node]: # 해당 노드의 인접 노드들에 대해서
                if i not in que: # 아직 큐에 들어가지 않았다면            
                    que.append(i) # 대기 큐에 넣어준다. 

    return 



# ------- 입력 부분 -------
V, E, s = map(int, input().split()) # Vertex, Edge, source(시작점)
graph = AdjacencyList(V, E)
# ------- 출력 부분 -------
DFS_stack(graph, s)
print()
DFS_recursion(graph, s, []) # visited에 빈 배열 선언
print()
BFS(graph, s)
