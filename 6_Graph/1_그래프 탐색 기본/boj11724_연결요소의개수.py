# 문제: 연결요소의 개수 (실버 2)
'''
1. 유니온 파인드
-------------------
2. BFS, DFS
for 모든 정점:
    - 만약 집합에 존재하는 정점이라면: pass
    - 집합에 존재하지 않는 정점이라면:
        dfs -> 탐색되는 모든 노드 집합에 넣기

--------------------
방문 여부를 list.append() 가 아니라 TRUE/FALSE로 하면 속도가 빨라짐

'''
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

# 그래프 생성
graph = {}
for i in range(N+1):
    graph[i] = []

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs 정의 
def dfs(vertex, visited):
    visited[vertex] = True # 방문 처리
    component.append(vertex) # 집합에 추가하기

    for i in graph[vertex]: # 인접노드에 대해서
        if not visited[i]: # 아직 방문하지 않았다면
                dfs(i, visited) # 방문
    
    return

# 모든 정점에 대해 체크
visited = [False] * (N+1)
components = []
for vertex in graph:
    # 아직 방문 안했다면 기존 집합에 없다는 것
    if not visited[vertex]:
        component = []
        dfs(vertex, visited)
        components.append(component)

print(len(components)-1) # 0 제외




    
