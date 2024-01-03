# 문제: 에디터 (실버 2)
'''
인덱스 기반으로 배열의 삽입, 삭제를 해야하는 문제
근데 그냥 list는 삽입, 삭제 모두 O(n)으로 시간 복잡도가 높다. 
반면 문제의 input은 크다. (배열의 초기 크기 10만개, 명령어 개수 50만개)

커서를 기준으로 왼쪽 큐, 오른쪽 큐 만들기
    - 커서 이동시마다 왼쪽 큐 pop -> 오른쪽 큐 || 왼쪽 큐 <- 오른쪽 큐 pop
    - cmd가 B 라면 왼쪽 큐에서 pop
'''
from collections import deque
# import sys
# input = sys.stdin.readline

editor = list(map(str, input().rstrip()))
M = int(input())

len_editor = len(editor)
cursor = len_editor

for i in range(M):
    cmd = input()  

    if cmd == 'L' or cmd == 'B':
        if cursor:
            cursor -= 1
        
        if cmd == 'B':
            del editor[cursor]            
        
        print(f'커서: {cursor}, cmd: {cmd}, editor: {editor}')           
        continue

    if cmd == 'R':
        if cursor <= len_editor:
            cursor += 1 
        print(f'커서: {cursor}, cmd: {cmd}, editor: {editor}')   
                
        continue

    editor.insert(cursor, cmd[2])        
    print(f'커서: {cursor}, cmd: {cmd}, editor: {editor}')   

print(editor)




