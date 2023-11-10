# 문제: 종이의 개수 (실버 2)
'''
색종이 자르기와 유사한 접근

3x3 분할
(구역)
1 2 3
4 5 6
7 8 9

'''
import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int,input().split()))for i in range(N)]

result = [0, 0, 0] # 0, 1, -1 순서로 저장됨

def dnq(y, x, size):
    number = graph[y][x] # 해당 종이 숫자 기록하기
    
    for i in range(y, y + size):
        for j in range(x, x + size):
            if graph[i][j] != number:
                s = size//3
                # 주의: i, j가 아니라 y, x 기준으로 돌아야 됨
                # 각 인덱스 단위가 아니라 블록 단위로 판단해야하기 때문
                dnq(y, x, s) # 1번 구역
                dnq(y, x+s, s) # 2번 구역
                dnq(y, x+2*s, s) # 3번 구역
                
                dnq(y+s, x, s) # 4번 구역
                dnq(y+s, x+s, s) # 5번 구역
                dnq(y+s, x+2*s, s) # 6번 구역
                
                dnq(y+2*s, x, s) # 7번 구역
                dnq(y+2*s, x+s, s) # 8번 구역
                dnq(y+2*s, x+2*s, s) # 9번 구역
                return

    
    result[number] += 1

dnq(0, 0, N)
print(result[-1])
print(result[0])
print(result[1])


