'''
<<Kruskal 알고리즘에서 사용되는 유니온-파인드 자료구조 연습>>

[Union-Find 핵심 연산과 최적화 기법]

make_set(n)
    - n = 초기화 하려는 노드의 개수

union(parent, rank, i, j)
    - parent: 각 노드의 부모 정보
    - rank: 각 노드의 랭크
    - i, j: 합치고자 하는 두 노드의 번호. i와 j가 속한 트리를 합치게 된다.     
    
find(parent, i)
    - parent = 각 노드의 부모 노드 정보를 저장한 리스트
    - i: 루트 노드를 찾고자 하는 노드의 번호
'''
### 초기화 연산 ###
def make_set(n): 
    # 각 노드의 부모 노드 정보를 저장하는 리스트 (리스트를 사용했지만 트리를 구현한 것임)
    parent = [i for i in range(n)]  # 초기에는 모든 노드가 루트 노드이므로 자기 자신을 부모로 가진다.
    
    # 각 노드의 랭크 정보를 저장하는 리스트 (Union by rank 적용을 위해)
    rank = [0 for _ in range(n)]
    
    return parent, rank


### Union 연산 ###
def union(parent, rank, i, j):
    # i의 루트와 j의 루트를 찾음
    root_i = find(parent, i)
    root_j = find(parent, j)

    # 만일 두 노드가 이미 같은 집합이라면 union() 수행할 필요 X
    if root_i == root_j:
        return
    
    # Union by rank: 두 트리의 루트 노드의 랭크를 비교하여 작은 트리를 큰 트리 아래에 붙인다.
    if rank[root_i] < rank[root_j]: # 루트[j]의 랭크가 더 높다면
        parent[root_i] = root_j # 루트[i]의 부모를 자기 자신 -> 루트[j]로 할당
    elif rank[root_i] > rank[root_j]: # 루트[i]의 랭크가 더 높다면
        parent[root_j] = root_i # 루트[j]의 부모를 자기 자신 -> 루트[i]로 할당
    else: # 두 루트의 랭크가 같다면
        parent[root_j] = root_i # 둘 중 하나(일반적으로 더 낮은 수)의 밑으로 통합시키고
        rank[root_i] += 1  # 트리 높이를 1 증가. (높이가 같은 걸 밑으로 붙였으니, 트리의 꼬리(?)가 더 길어짐)


### Find 연산  ###
def find(parent, i):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[i] != i:
        parent[i] = find(parent, parent[i])  # 경로 압축 (만나는 노드의 부모 노드를 루트 노드로 바꿔주기)
    # 자기 자신을 가리키면 루트 노드 (parent[i] == i)
    return parent[i]


#### Find 연산 (경로 압축 X 버전) ###
# 실제로 쓸 일은 없으니 이해용으로만 보기! 
def find(parent, i):
    # 루트 노드가 아니라면 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[i] != i:
        find(parent, parent[i])  
    # 자기 자신을 가리키면 루트 노드 (parent[i] == i)
    return i

