# 문제: 스택 (실버 4)
import sys
input = sys.stdin.readline

def stack(stk, cmd):
    if cmd[0] == "push":        
        X = int(cmd[1])
        stk.append(X)
        
    if cmd[0] == "pop":
        if len(stk) == 0:
            print(-1)
        else:
            item = stk.pop()
            print(item)

    if cmd[0] == "size":        
        print(len(stk))

    if cmd[0] == "empty":
        if len(stk) == 0:
            print(1)
        else:
            print(0)

    if cmd[0] == "top":
        if len(stk) == 0:
            print(-1)
        else:
            print(stk[-1])
    


### 입력 부분 ###
stk = []
for i in range(int(input())):
    cmd = list(input().split())
    stack(stk, cmd)