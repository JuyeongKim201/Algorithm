# 문제: 트럭 (맞았습니다)
'''
2개의 큐 활용 (trucks, bridge)
- while문으로 cnt 세기 (큐가 빌 때까지)
- bridge는 0(빈 도로)과 트럭 i 로 채워져 있음. 
- trucks에 있는 트럭을 하나씩 뺀다. -> bridge에 넣어주기
- i번째 트럭이 bridge에 들어왔을 때 총합이 L을 초과하면 i번째 트럭을 넣지 않음

[교훈: sum 같은 내장함수 이름을 변수명으로 하지 말자..!]
'''
import sys
input = sys.stdin.readline
from collections import deque

n, w, L = map(int,input().split())
trucks = deque(list(map(int,input().split())))
bridge = deque(0 for i in range(w))
print(f'bridge: {bridge}')

cnt = 0
weight = 0
while bridge or trucks:
    out = bridge.popleft()
    weight -= out
    if trucks: # 대기중인 트럭이 있다면
        if L >= weight + trucks[0]:
            truck = trucks.popleft()
            bridge.append(truck)
            weight += truck
        else:
            bridge.append(0)
    
    cnt += 1

print(cnt)

