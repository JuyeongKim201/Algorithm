# 문제: 바이러스 (실버 3)
'''
주어진 컴퓨터에서 시작해서 dfs, bfs 돌리면 되는 문제.
이번에는 bfs로 구현 ㄱㄱ
-------------------
<수정 버전1>
1. infected를 배열로 담지 않고 바로 카운트
2. 전역변수 줄이기: que, visited, infected 선언을 bfs() 함수 내에서 초기화 (재귀 돌리는게 아니라 괜찮음)
3. 수정은 안했지만, graph, que, visited 등을 밖에서 선언할 거면 함수 인자로 넣어주는게 함수 재사용성이 좋음
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque

V = int(input())
E = int(input())

graph = {i: [] for i in range(V+1)}

for i in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(start):
    que = deque()
    visited = [False] * (V+1)
    infected = 0
    
    que.append(start)

    while que:
        current = que.popleft()
        if not visited[current]:
            visited[current] = True
            infected += 1

            for i in graph[current]:
                que.append(i)
    
    return infected
            
print(bfs(1)-1)    

