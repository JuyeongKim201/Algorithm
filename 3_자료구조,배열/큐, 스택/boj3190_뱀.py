# 문제: 뱀 (골드 4)
'''
    - '-1' 로 둘러싸인 벽 만들기 // 뱀의 몸통도 '-1'
    - 뱀의 몸통이 있는 위치를 튜플 형태로 큐에 넣어 관리하기
    - 뱀의 몸통에 push 된 좌표는 지도 상 -1 처리, 뱀의 몸통에서 popleft된 좌표는 지도 상 0 처리
    - 움직임 1: 머리가 이동 // 움직임 2: 꼬리가 따라오거나 or (사과 먹었을 경우) 꼬리는 그대로
    - 움직임 1에서 -1을 만나면 게임 끝, cnt 반환
'''
import sys
from collections import deque
input = sys.stdin.readline

# 그래프 만들기
N = int(input())
graph = [list(-1 for i in range(N+2))]
for i in range(N):
    graph.append([-1] + list(0 for i in range(N)) + [-1])
graph.append(list(-1 for i in range(N+2)))

# 사과 위치 받기
K = int(input()) 
for i in range(K):
    r, c = map(int, input().split())
    graph[r][c] = 1

# 방향 전환 정보 받기
L = int(input())
change_direction = [False]*(N**2+1)
for i in range(L):
    second, chg = map(str, input().split())
    change_direction[int(second)] = chg

# snake !!
snake = deque()
snake.append([1,1])


# 초기 세팅
graph[1][1] = -1
next = [1,2]
tmp = [1,2]
direction = 'right'
cnt = 0

while graph[tmp[0]][tmp[1]] != -1:    
    flag = False # 방향 전환 신호    
    
    next[0] = tmp[0]
    next[1] = tmp[1]

    # 뱀 꼬리 이동
    if graph[next[0]][next[1]] == 0: # 사과 못 먹으면        
        prev = snake.popleft() # 꼬리 따라오기        
        graph[prev[0]][prev[1]] = 0 # 지나간 자리는 다시 0으로    
    
    # 뱀 머리 이동
    snake.append([next[0],next[1]])
    graph[next[0]][next[1]] = -1

    # 방향 전환을 만났는가?
    if change_direction[cnt]:
        flag = True
        rotate = change_direction[cnt] # 회전 방향 기록
    
    # 다음 step 밟기
    if direction == 'right':
        if flag:
            if rotate == 'L': # 좌회전이라면
                direction = 'up' # up 방향 진행
                tmp[0] -= 1 # 위로 한 칸 
                cnt += 1
                continue
            else:
                direction = 'down' # down 방향 진행
                tmp[0] += 1 # 아래로 한 칸  
                cnt += 1       
                continue
        
        tmp[1] += 1 # 오른쪽 직진
        
    elif direction == 'left':
        if flag:
            if rotate == 'L': # 좌회전이라면
                direction = 'down' # down 방향 진행
                tmp[0] += 1 # 아래로 한 칸  
                cnt += 1       
                continue
            else:
                direction = 'up' # up 방향 진행
                tmp[0] -= 1 # 위로 한 칸 
                cnt += 1
                continue
        
        tmp[1] -= 1 # 왼쪽 직진

    elif direction == 'up': 
        if flag:
            if rotate == 'L': # 좌회전이라면
                direction = 'left' # left 방향 진행
                tmp[1] -= 1 # 왼쪽으로 한 칸
                cnt += 1         
                continue
            else:
                direction = 'right' # right 방향 진행
                tmp[1] += 1 # 오른쪽으로 한 칸 
                cnt += 1
                continue
        
        tmp[0] -= 1 # 위로 직진
    
    elif direction == 'down': 
        if flag:
            if rotate == 'L': # 좌회전이라면
                direction = 'right' # right 방향 진행
                tmp[1] += 1 # 오른쪽으로 한 칸   
                cnt += 1      
                continue
            else:
                direction = 'left' # left 방향 진행
                tmp[1] -= 1 # 오른쪽으로 한 칸 
                cnt += 1
                continue
        
        tmp[0] += 1 # 아래로 직진
    
    cnt += 1
    

print(cnt)

