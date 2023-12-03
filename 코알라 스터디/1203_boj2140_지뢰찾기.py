# 문제: 지뢰찾기 (골드 4)
'''
- 지뢰를 마크하면 인접 칸들의 count를 내린다.
- 인접 칸 중 0이 있으면 지뢰를 마크할 수 없다. 

- 맨 위 칸부터 내려오기 (N-queen 느낌)
    - 사방 8개 칸 모두 검사
    - '#'이면 무시
    - 대각선이 1이면 무조건 놓기
    - ...
------------------------------------------
    - 맨 위 칸: 
        양끝: 대각선 위가 1이면 mark 아니면 x
        중간: 좌상, 상, 우상 숫자 고려하면서 mark
    - 맨 아래 칸:
        양끝: 대각선 아래가 1이면 mark 아니면 x
        중간: 좌상, 상, 우상 숫자 고려하면서 mark
    - 중간 칸들:
        왼쪽끝: 좌상, 좌, 좌하 체크 // 오른쪽도 마찬가지
        가운데: 무조건 놓기
'''
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(str, input().rstrip())) for i in range(N)]
for i in range(N):
    for j in range(N):
        if graph[i][j] == '0': graph[i][j] = 0
        if graph[i][j] == '1': graph[i][j] = 1
        if graph[i][j] == '2': graph[i][j] = 2
        if graph[i][j] == '3': graph[i][j] = 3

''' # 부분에 대해서 '''
for i in range(1, N-1):
    for j in range(1, N-1):
        if i == 1: # 맨 위 칸
            print()
        elif i == N-2: # 맨 아래 칸
            print()
        else: # 중간 칸
            print()

# 마크하고 카운트 체크하는 함수
def mark(line):
    if line = 

