'''
MST를 구하는 Kruskal 알고리즘 연습
'''

# 필요한 함수들을 먼저 정의합니다.

def find(parent, i):
    """노드 i의 루트 노드를 찾는 함수"""
    if parent[i] != i:
        parent[i] = find(parent, parent[i])  # 경로 압축
    return parent[i]

def union(parent, rank, i, j):
    """두 노드 i와 j를 포함하는 두 트리를 합치는 함수"""
    root_i = find(parent, i)
    root_j = find(parent, j)
    
    if rank[root_i] < rank[root_j]:
        parent[root_i] = root_j
    elif rank[root_i] > rank[root_j]:
        parent[root_j] = root_i
    else:
        parent[root_j] = root_i
        rank[root_i] += 1

def kruskal(graph):
    """Kruskal 알고리즘을 사용하여 MST를 찾는 함수"""
    edges = []
    # 그래프의 모든 간선과 가중치를 리스트로 변환
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors:
            if (neighbor, node, weight) not in edges:  # 중복 간선 제거
                edges.append((node, neighbor, weight))
    # 간선들을 가중치 기준으로 정렬
    edges.sort(key=lambda x: x[2])
    
    parent = [i for i in range(len(graph))]  # 초기에 각 노드는 자기 자신을 부모로 가짐
    rank = [0] * len(graph)
    mst = []
    
    for edge in edges:
        node1, node2, weight = edge
        if find(parent, node1) != find(parent, node2):  # 두 노드의 루트가 다르면
            mst.append(edge)
            union(parent, rank, node1, node2)  # 두 노드를 포함하는 트리를 합침
    
    return mst


##### 테스트 #####
# 테스트를 위한 그래프
graph = {
    0: [(1, 7), (2, 5)],
    1: [(0, 7), (2, 8), (3, 9)],
    2: [(0, 5), (1, 8), (3, 7)],
    3: [(1, 9), (2, 7), (4, 5), (5, 7)],
    4: [(3, 5), (5, 8), (6, 9)],
    5: [(3, 7), (4, 8)],
    6: [(4, 9)]
}

# Kruskal 알고리즘 실행
mst_result = kruskal(graph)
print(mst_result)

