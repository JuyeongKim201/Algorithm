# 문제: 이분 그래프 (골드 4)
'''
0. 테스트 케이스 별로 V, E 따로 받고 문제 해결 -> 케이스 나누기만 하면 됨
----------------------
[이분 그래프 판별]
- 현재 노드 칠하기 (1 또는 0)
- 만일 인접 노드 중에 같은 색이 있다면: return NO
- dfs로 자식 노드 끝까지 방문
    - 다음 노드를 방문할 때는 현재 노드와 다른 색으로 칠하기
    (현재 노드 색에 따라서 0 또는 1 넘겨주기)
----------------------
[주의할 점]
1. 연결 리스트가 주어지는가? 그게 아니라면 아무 정점이나 루트로 설정할 수 X
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(node, color):
    global result 

    color_list[node] = color # 부모와 다르게 색칠하기
    visited[node] = True # 방문 처리
    # 인접 노드와 색 겹치는지 검사
    for i in graph[node]:
        if color_list[i] == color_list[node]:
            result = False
            return
    
    # 안 겹친다면, 다음 노드들에 대해 재귀적으로 색칠하기
    for i in graph[node]:
        if not visited[i]:
            # 현재 노드와 다른 색 넘겨주기
            if color_list[node] == 0:
                dfs(i, 1)
            else:
                dfs(i, 0)
    
    return 
        

### 입력 부분 ###
T = int(input())
for i in range(T):
    V, E = map(int, input().split())
    graph = {i:[] for i in range(V+1)}
    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    color_list = [-1 for i in range(V+1)]
    visited = [False]*(V+1)
    result = True

    # 연결 리스트가 아닐 수도 있기 때문에 모든 정점에 대해서 검사
    for i in range(1, V+1):
        if not visited[i]:
            dfs(i, 0)
    
    if result:
        print("YES")
    else:
        print("NO")
    

