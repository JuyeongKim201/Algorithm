# 문제: 색종이 만들기 (2차)
'''
1 2
3 4
'''
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split()))for _ in range(N)]
result = [0,0] # 하얀색(0), 파란색(1) 개수 저장

def dnq(y, x, n):
    color = graph[y][x]
    for i in range(y, y+n):
        for j in range(x, x+n):
            if graph[i][j] != color:
                next = n//2
                dnq(y, x, next) # 파트 1
                dnq(y, x+next, next) # 파트 2
                dnq(y+next, x, next) # 파트 3
                dnq(y+next, x+next, next) # 파트 4
                return
    
    result[color] += 1

dnq(0, 0, N)                
print(result[0])
print(result[1])



