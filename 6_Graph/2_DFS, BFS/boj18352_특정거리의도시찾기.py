# 문제: 특정 거리의 도시 찾기 (실버 2)
'''
(미로 탐색과 유사한 접근)
- bfs로 최단 거리 탐색
- graph: 인접행렬법으로 그래프 구성
    - 해당 도시 갈 수 있는지 여부는 그래프를 통해 확인
- visited 배열: 각 도시 방문 여부
- distance 배열: [출발지 -> 각 도시] 까지의 거리 기록

(도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X)

------------
<메모리 초과!!>
파이썬 list의 각 인덱스는 8byte 차지 (32비트 파이썬에선 4byte)
input 최댓값은 N = 300,000 ^2 -> N^2 = 9e10
900억 byte -> 90gb 정도?? 메모리 소모한다는 계산....

------------
<수정 ver>
1. 인접행렬에서 인접리스트로 바꾸니까 통과 (메모리 측면 이득)
2. defaultdict 컬렉션 활용
'''
import sys
input = sys.stdin.readline
from collections import deque, defaultdict

N, M, K, X = map(int, input().split())
graph = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)


def bfs(graph, city):
    visited = [False]*(N+1)
    distance = [0]*(N+1)

    que = deque()
    que.append(city)
    visited[city] = True # 출발지 도착 표시

    while que:
        current = que.popleft()
        for next in graph[current]:
            # 아직 방문하지 않았다면,
            if not visited[next]: 
                que.append(next)
                distance[next] = distance[current]+1
                visited[next] = True                
    
    return distance, visited

distance, visited = bfs(graph, X)

result = []
for city in range(len(distance)):
    if distance[city] == K:
        result.append(city)

if result:
    for i in result:
        print(i)
else:
    print(-1)        


