# 문제: 아침 산책 (골드 3)
'''
1. 산책의 시작점과 끝점은 모두 실내여야 한다
2. 산책 도중에 실내 장소를 거치면 안된다
3. 트리 구조: 두 점 사이의 경로는 유일!
----------------------------------
[풀이 아이디어]

1. 모든 (시작점, 끝점) 조합 얻기 (permutations)
    - 이때, 시작점, 끝점은 실내여야 한다.
2. 각 (시작점, 끝점)에 대해 경로 탐색 및 실내 체크
    - 시작점에서 출발 -> 끝점까지 dfs -> 경로 저장
    - 자식 노드가 없다면 현재 탐색중인 가지는 x
    - 경로 안에 실내가 있으면 해당 경로는 폐기한다.
'''
from itertools import *
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
indoor = [False] + list(map(int, input().rstrip()))

graph = {i:[] for i in range(1, N+1)}
for i in range(N-1):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 1. 모든 (시작점, 끝점) 조합 얻기 (permutations)
start_end = []
for i in permutations(graph, 2):
    if indoor[i[0]] == 1 and indoor[i[1]] == 1: # 시작점 or 끝점이 실외인 경우 받지 않음
        start_end.append(i)

# dfs 정의
def dfs(start, node, end):
    global departure
    global escape
    
    # 탈출 조건: 도착지에 도착함
    if node == end:
        departure = True
        path.append(node) # 되돌아가며 경로에 추가
        return
    
    visited[node] = True

    for i in graph[node]:
        if not visited[i]:
            dfs(start, i, end)

            # 탈출 조건2: 경로 상에 실내가 포함됨
            if escape:
                return
            
            if departure:
                # 만일 해당 경로가 시작점이 아닌데 실내라면
                if node != start and indoor[node] == 1:
                    escape = True
                    return

                path.insert(0, node) # 되돌아가며 경로에 추가 (편의상 거꾸로 추가)
                return
    
# 다른 경로의 수
cnt = 0

# 2. 각 (시작점, 끝점)에 대해 경로 탐색 및 실내 체크
for combi in start_end:
    visited = [False]*(N+1)
    start, end = combi[0], combi[1]
    departure = False # 도착지 방문시 탈출 조건
    
    # 해당 조합에 대한 경로 뽑기
    path = []
    escape = False
    dfs(start, start, end)

    if escape:
        continue

    # 실내 검사 통과!
    cnt += 1
            
print(cnt)