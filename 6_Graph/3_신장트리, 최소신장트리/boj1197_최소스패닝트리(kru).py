# 문제: 최소 스패닝 트리 (골드 4)
'''
[MST 찾기] - Kruskal's Algorithm
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

V, E = map(int, input().split())

# 간선 정보 초기화 + 정렬
edges = [] 
for i in range(E):
    edges.append(list(map(int,input().split())))

edges.sort(key=lambda x: x[2]) # '2번 인덱스 = 가중치'를 기준으로 간선들을 정렬


# make-set
parent = [i for i in range(V+1)] # union-find 트리 (부모 정보)
rank = [0 for i in range(V+1)] # 랭크 정보 담기

# find 함수 정의
def find(x):
    if parent[x] != x: # 루트 노드가 아니라면
        parent[x] = find(parent[x]) # 재귀적으로 탐색 + 경로 압축
    return parent[x] # 루트 노드 return

# union 함수 정의
def union(x, y):
    root_x = find(x)
    root_y = find(y)

    # union-by-rank
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y
        rank[root_x] += 1


totalCost = 0
for edge in edges:
    node_one, node_two, weight = edge[0], edge[1], edge[2]
    if find(node_one) != find(node_two): # 사이클을 형성하지 않는다면 (같은 트리에 속해있지 않다면)
        union(node_one, node_two) # 경로에 추가 (같은 트리로 합치기)
        totalCost += weight

print(totalCost)



