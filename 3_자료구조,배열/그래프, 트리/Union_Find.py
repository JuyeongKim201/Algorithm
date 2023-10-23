'''
<<Kruskal 알고리즘에서 사용되는 유니온-파인드 자료구조 연습>>

[Union-Find 핵심 연산과 최적화 기법]

make_set(n)
    - n = 초기화 하려는 노드의 개수

find(parent, i)
    - parent = 각 노드의 부모 노드 정보를 저장한 리스트
    - i: 루트 노드를 찾고자 하는 노드의 번호

union(parent, rank, i, j)
    - parent: 각 노드의 부모 정보
    - rank: 각 노드의 랭크
    - i, j: 합치고자 하는 두 노드의 번호. i와 j가 속한 트리를 합치게 된다. 

'''
# 초기화 연산
def make_set(n): 
    # 각 노드의 부모 노드 정보를 저장하는 리스트
    # 초기에는 모든 노드가 루트 노드이므로 자기 자신을 부모로 가진다.
    parent = [i for i in range(n)]
    
    # 각 노드의 랭크 정보를 저장하는 리스트 (Union by rank 적용을 위해)
    rank = [0 for _ in range(n)]
    
    return parent, rank


# Find 연산 
def find(parent, i):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[i] != i:
        parent[i] = find(parent, parent[i])  # 경로 압축 (만나는 노드의 부모 노드를 루트 노드로 바꿔주기)
    # 자기 자신을 가리키면 루트 노드 (parent[i] == i)
    return parent[i]


# Find 연산 (경로 압축 X 버전 - 실제로 쓸 일은 없으니 이해용으로만 보기)
def find(parent, i):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[i] != i:
        find(parent, parent[i])  
    # 자기 자신을 가리키면 루트 노드 (parent[i] == i)
    return i



# Union 연산 
def union(parent, rank, i, j):
    root_i = find(parent, i)
    root_j = find(parent, j)
    
    # Union by rank: 두 트리의 루트 노드의 랭크를 비교하여 작은 트리를 큰 트리 아래에 붙인다.
    if rank[root_i] < rank[root_j]:
        parent[root_i] = root_j
    elif rank[root_i] > rank[root_j]:
        parent[root_j] = root_i
    else:
        parent[root_j] = root_i
        rank[root_i] += 1  # 랭크가 같을 때 하나의 트리 높이를 1 증가시킨다.



# 사용 예시
n = 5  # 5개의 노드
parent, rank = make_set(n)

union(parent, rank, 0, 1)
union(parent, rank, 1, 2)

print(find(parent, 0))  # 0, 1, 2가 같은 집합에 속하므로 같은 루트를 반환해야 함
print(find(parent, 2))



'''

'''



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
