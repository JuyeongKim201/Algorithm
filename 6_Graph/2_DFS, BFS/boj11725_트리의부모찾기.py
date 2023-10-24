# 문제: 트리의 부모 찾기 (실버 2)
'''
1. 그래프 만들기
2. 1번 노드부터 시작해서 dfs 돌리기 -> 다음 재귀로 넘어갈 때 [기존 노드:다음 노드] = [부모:자식]
3. 저장한 [부모:자식] 테이블 출력하기
'''

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 그래프 받기
N = int(input())
graph = {i:[] for i in range(N+1)}
for i in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# [부모:자식] 테이블 <- index = 자식 노드, value = 부모 노드
parents = [0 for i in range(N+1)]

# dfs 정의
visited = [False] * (N+1)
def dfs(node):
    visited[node] = True
    for i in graph[node]:
        if not visited[i]:
            parents[i] = node
            dfs(i)

### 출력 부분 ### 
dfs(1)
for i in range(2, N+1):
    print(parents[i])

