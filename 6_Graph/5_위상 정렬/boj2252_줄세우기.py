# 문제: 줄 세우기 (골드 3)
'''
(문제 이해)
1. 두 학생 간에는 순서(방향)가 주어짐
2. 키 비교라는 특성상 사이클이 형성될 수 없음
    -> DAG 형성
3. N = 정점의 수, M = 간선의 수
'''
import sys
input = sys.stdin.readline
from collections import deque

V, E = map(int, input().split())

indegree = [0 for i in range(V+1)] # 각 노드의 indegree 정보 -> 0으로 초기화
graph = [[] for i in range(V+1)] # 간선 정보를 담기 위한 배열

for i in range(E):
    A, B = map(int, input().split())
    graph[A].append(B) # A 학생 키 < B 학생 키 (줄 순서: A -> B)
    indegree[B] += 1

def topological_sort(graph):
    que = deque()
    result = []

    # indegree가 0인 학생 담기
    for student in range(1, V+1): 
        if indegree[student] == 0:
            que.append(student)

    # 큐가 빌 때까지
    while que:
        # 큐에서 하나씩 빼면서, 해당 학생과 연결된 간선 제거        
        current = que.popleft()
        result.append(current)

        for friend in graph[current]:
            indegree[friend] -= 1

            if indegree[friend] == 0:
                que.append(friend)

    return result

### 출력 부분 ###
result = topological_sort(graph)
for i in result:
    print(i, end=' ')

