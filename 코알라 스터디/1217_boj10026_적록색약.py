# 적록색약 (골드 5)
'''
그래프 만들기
    - 0으로 경계선 둘러싸기
    - 색약 ver 그래프 만들기 (G를 모두 R로)
bfs 탐색
    - 상하좌우 검사 
    - 같으면 0으로 만들기
'''
import sys
input = sys.stdin.readline

n = int(input())
graph = []
graph_rg = []

graph.append([0]*(n+2))
graph_rg.append([0]*(n+2))
for i in range(n):
    tmp = list(map(str,input().rstrip())) 
    graph.append([0] + tmp + [0])
    graph_rg.append([0] + tmp + [0])    
graph.append([0]*(n+2))
graph_rg.append([0]*(n+2))

for i in range(len(graph_rg)):
    for j in range(len(graph_rg[i])):
        if graph_rg[i][j] == 'G':            
            graph_rg[i][j] = 'R'

def bfs(graph, i, j, cnt):
    if graph[i][j] == 0:
        return
    else:
        graph[i][j] = 0
        bfs(graph, i-1, j) # 상
        bfs(graph, i+1, j) # 하
        bfs(graph, i, j-1) # 좌
        bfs(graph, i, j+1) # 우

    return cnt+1

cnt = 0
cnt_rg = 0
for i in range(len(graph)):
    for j in range(len(graph[i])):
        cnt = cnt + bfs(graph, i, j, cnt)
        cnt_rg = cnt_rg + bfs(graph_rg, i, cnt_rg)

print(cnt, cnt_rg)




