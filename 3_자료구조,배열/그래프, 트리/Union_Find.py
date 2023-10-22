'''
Kruskal 알고리즘에서 사용되는 유니온-파인드 자료구조 연습
'''

# # Union-Find 클래스 정의
# class UnionFind:
#     def __init__(self, n):
#         self.parent = [i for i in range(n)]
#         self.rank = [0] * n  # 트리의 높이를 저장하는 목적

#     # Find 연산 (경로 압축 포함)
#     def find(self, x):
#         if self.parent[x] != x:
#             self.parent[x] = self.find(self.parent[x])  # 경로 압축
#         return self.parent[x]

#     # Union 연산
#     def union(self, x, y):
#         root_x = self.find(x)
#         root_y = self.find(y)

#         if root_x != root_y:
#             # 높이가 더 낮은 트리를 높이가 더 높은 트리에 붙입니다. 
#             # 이렇게 하면 트리의 높이가 최대한 작아집니다.
#             if self.rank[root_x] > self.rank[root_y]:
#                 root_x, root_y = root_y, root_x
#             self.parent[root_x] = root_y
#             if self.rank[root_x] == self.rank[root_y]:
#                 self.rank[root_y] += 1


graph = {
    1: [(2, 3), (3, 1)],   # (노드, 가중치)
    2: [(1, 3), (3, 3), (4, 1)],
    3: [(1, 1), (2, 3), (4, 2)],
    4: [(2, 1), (3, 2)]
}

# Union-Find 자료구조 정의
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)
    
    # 두 노드의 루트 노드의 랭크를 비교하여 작은 랭크의 루트를 큰 랭크의 루트에 연결
    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    elif rank[rootX] > rank[rootY]:
        parent[rootY] = rootX
    else:
        parent[rootY] = rootX
        rank[rootX] += 1

# Kruskal 알고리즘 정의
def kruskal(graph):
    result = []  # 결과를 담을 리스트
    i, e = 0, 0

    # 그래프의 간선들을 가중치 기준으로 정렬
    edges = []
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            edges.append((weight, node, neighbor))
    edges.sort()

    parent = {}
    rank = {}

    # 각 노드에 대해 parent를 자신으로 초기화
    for node in graph:
        parent[node] = node
        rank[node] = 0

    while e < len(graph) - 1:
        weight, src, dest = edges[i]
        i += 1
        x = find(parent, src)
        y = find(parent, dest)

        # 사이클이 발생하지 않는 경우에만 간선을 추가
        if x != y:
            e += 1
            result.append((src, dest, weight))
            union(parent, rank, x, y)

    return result

# 출력
mst = kruskal(graph)
print("Minimum Spanning Tree:")
for u, v, w in mst:
    print(f"{u} - {v} (가중치: {w})")
