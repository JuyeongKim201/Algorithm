'''
<위상 정렬 알고리즘 - 큐를 활용하는 kahn's algorithm 연습>
----------------------------------------------------------
[위상 정렬의 특징]
1. 위상 정렬은 DAG에 대해서만 수행할 수 있다.
    - DAG(Direct Acyclic Graph): 비순환 방향 그래프

2. 위상 정렬은 여러가지 답이 존재할 수 있다.
    - 한 단계에서 큐에 새롭게 들어가는 원소가 2개 이상이라면 경우의 수가 나뉘게 된다.

3. 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있다.
    - 사이클에 포함된 원소 중에서 어떤 원소도 큐에 들어가지 못한다.
----------------------------------------------------------
[kahn's Algorithm]
칸 알고리즘은 큐를 활용하는 위상 정렬 알고리즘이다.
동작 과정은 다음과 같다.

1. indegree가 0인 모든 노드를 큐에 넣는다.
2. 큐가 빌 때까지 다음 과정을 반복적으로 수행한다.
    1) 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다.
    2) 새롭게 indegree가 0이 된 노드를 큐에 넣는다. 

    => 결과적으로, '각 노드가 큐에 들어온 순서 == 위상 정렬을 수행한 결과'가 된다.
----------------------------------------------------------
'''

from collections import deque

# 노드 개수와 간선 개수 입력받기
V, E = map(int,input().split())
# 모든 노드에 대한 indegree 배열 초기화
indegree = [0]*(V+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(V+1)]

# 방향 그래프의 모든 간선 정보 입력받기
for i in range(E):
    x, y = map(int, input().split())
    graph[x].append(y) # 정점 x -> y 방향으로 이동 가능
    indegree[y] += 1 # y의 indegree 값 1 증가

# 위상 정렬 함수
def kahn(graph):
    result = [] # 정렬 수행 결과를 담을 리스트
    que = deque() # 큐 세팅

    # 1. indegree가 0인 모든 노드를 큐에 넣는다.
    for i in range(1, V+1):
        if indegree[i] == 0:
            que.append(i)
    
    # 2. 큐가 빌 때까지 다음 과정을 반복적으로 수행한다.
    while que:
        # 1) 큐에서 원소를 꺼내 해당 노드에서 나가는 간선을 그래프에서 제거한다.
        print(f'큐: {que}', end=' -> ')
        current = que.popleft() # 큐에서 원소 꺼내기
        result.append(current) # 결과에 추가
        print(f'(pop {current}) -> {que} || result: {result}')
        
        
        for i in graph[current]: # 현재 노드가 가리키는 노드들에 대해 
            indegree[i] -= 1 # indegree 값 1 감소

            # 2) 새롭게 indegree가 0이 된 노드를 큐에 넣는다. 
            if indegree[i] == 0:
                que.append(i)
        
    return result



# 결과 출력
print(graph)

result = kahn(graph)
for i in result:
    print(i, end=' ')



