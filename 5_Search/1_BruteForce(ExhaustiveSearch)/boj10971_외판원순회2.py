# 문제: 외판원 순회2 (실버 2)

'''
---------------------------------
base case: 모든 도시를 탐색함
   - 비용 ++ // totalCost가 최소인지 비교하기
   - 출발지로 돌아온다.

general case: 
   - 모든 출발지에 대해 탐색
   - n번째 이동에 성공했다면, n+1번째 이동에 성공하는 법은 다음과 같음
       1. 이미 방문 했다면 방문 x
       2. 비용 행렬에서 [현재 도시][도착 도시] == 0 이라면 방문 x
   - 방문 성공시: 
       - 해당 도시 방문 체크
       - 비용 ++ 
---------------------------------
백트랙킹의 핵심: 
"현재 상태에서의 해가 유망한지 (promising)를 검사하고, 유망하지 않다면 해당 경로를 더 이상 탐색하지 않는 것"
---------------------------------
'''

import sys
sys.setrecursionlimit(10**6)

# 입력 받기
N = int(input())

costs = []
for i in range(N):
    costs.append(list(map(int,input().split())))

# 최소 총경비 변수 세팅
min_totalCost = 0
for cost in costs:
    min_totalCost += sum(cost)


def travel(n, departure, totalCost):
        global min_totalCost

        if n == N:
            if costs[departure][startingPoint] != 0:  # 출발지로 돌아올 수 있는 경우에만
                totalCost += costs[departure][startingPoint]
                if totalCost < min_totalCost:
                    min_totalCost = totalCost
            return 
        
        if totalCost >= min_totalCost: # 지금까지의 경비가 이미 최소 경비를 초과했다면
            return
        

        for arrival in range(N): # 가능한 모든 행선지에 대해
            if visitedCity[arrival]: # 이미 방문했다면 패스
                continue
            if costs[departure][arrival] == 0: # 방문할 수 없는 곳이면 패스
                continue
            
            # 위 조건을 통과했다면
            visitedCity[arrival] = True # 방문
            travel(n+1, arrival, totalCost + costs[departure][arrival]) # 다음 여행지로 출발
            visitedCity[arrival] = False # 탐색 후엔 흔적 지워주기

# 출발지로 모든 도시 고려
for startingPoint in range(N):
    visitedCity = [False for i in range(N)] # 도시 방문 체크 시작
    visitedCity[startingPoint] = True
    travel(1, startingPoint, 0)


print(min_totalCost)


