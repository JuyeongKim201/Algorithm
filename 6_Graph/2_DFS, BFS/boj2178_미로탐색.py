# 문제: 미로 탐색 (실버 1)
'''
가중치 없는 최단경로 찾기

[풀이 아이디어]
- bfs 방식으로 모든 방향(상하좌우) 탐색하기
- distance 지도 만들기
- directions 튜플 리스트를 통해 방향 조정

[주의]
- 행열과 x축, y축은 순서가 반대임. 변수 네이밍에서 조심..
'''
import sys
input = sys.stdin.readline
from collections import deque

def bfs(maze, N, M):    
    visited = [[False] * M for _ in range(N)] # 방문 여부
    distance = [[0] * M for _ in range(N)] # 시작점부터의 거리를 나타내는 지도
    
    # BFS를 위한 큐와 시작 위치
    que = deque([(0, 0)])
    visited[0][0] = True
    distance[0][0] = 1 
    
    # 상, 하, 좌, 우 이동 방향을 튜플로 저장
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)] 
    
    while que:
        y, x = que.popleft()
        # 튜플 언패킹 (tuple unpacking): 변수를 튜플의 요소 개수만큼 할당하면 각 튜플의 개별 요소를 할당함
        for dy, dx in directions: # 현재 좌표의 상하좌우 각 좌표들에 대해            
            ny, nx = y + dy, x + dx  # 해당 좌표
            

            # 미로 범위 내에 있고, 이동할 수 있는 칸이며, 아직 방문하지 않았다면
            if (0 <= ny < N and 0 <= nx < M) and (maze[ny][nx] == 1) and (not visited[ny][nx]):
                que.append((ny, nx))
                visited[ny][nx] = True # 방문                
                distance[ny][nx] = distance[y][x] + 1 # 이전 좌표의 거리+1
           
    return distance[N-1][M-1]

# 입력
N, M = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]


# 출력
print(bfs(maze, N, M))
