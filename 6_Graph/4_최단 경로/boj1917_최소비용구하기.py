# 문제: 최소비용 구하기 (골드 5)
'''
비가중치 그래프에서의 최단경로 -> bfs
가중치 그래프에서의 최단경로 -> dijkstra
이 문제는 가중치 방향 그래프
'''
import sys, heapq
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(graph, start, end):
    costs = {i:float('infinity') for i in range(1, N+1)}
    costs[start] = 0 # 거리 초기화

    pr_que = []
    heapq.heappush(pr_que, (0, start)) # 큐에 시작 노드 넣기

    while pr_que:
        current_cost, current_node = heapq.heappop(pr_que)

        if costs[current_node] < current_cost:
            continue

        for cost, adjacent in graph[current_node]:
            new_cost = current_cost + cost

            if new_cost < costs[adjacent]:
                costs[adjacent] = new_cost
                heapq.heappush(pr_que, (new_cost, adjacent))
    
    return costs[end]

### 입력 부분 ###
N = int(input())
M = int(input())
graph = defaultdict(list)
for i in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))

start, end = map(int, input().split())
print(dijkstra(graph, start, end))
