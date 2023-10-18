# 문제: 큐2 (실버 4)
'''
아마 list 구현보다 시간복잡도가 더 낮은 deque 구현을 하라는 문제
'''

from collections import deque
import sys
input = sys.stdin.readline


def queue(que, cmd):
    if cmd[0] == 'push':
        que.append(int(cmd[1]))
    
    elif cmd[0] == 'pop':
        if len(que) == 0:
            print(-1)
        else:            
            print(que.popleft())
    
    elif cmd[0] == 'size':
        print(len(que))
    
    elif cmd[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
    
    elif cmd[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    
    elif cmd[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])      



### 입력 파트 ###
N = int(input())
que = deque()
for i in range(N):
    cmd = list(input().split())
    queue(que, cmd)

