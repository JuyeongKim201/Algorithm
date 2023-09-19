# 문제: 스택 2
import sys
input = sys.stdin.readline
from collections import deque


N = int(input())

stack = deque([])

for i in range(N):
    cmd = input().rstrip()
    stackLen = len(stack)

    if len(cmd) > 2:
        stack.append(int(cmd[2:]))
    
    elif cmd == '2':
        if stackLen > 0:
            print(stack.pop())

        elif stackLen == 0:
            print(-1)        
        
    elif cmd == '3':
        print(stackLen)        

    elif cmd == '4':
        if stackLen == 0:
            print(1)

        else:
            print(0)
        

    if cmd == '5':
        if stackLen > 0: 
            print(stack[-1])
        
        elif stackLen == 0:
            print(-1)
        
