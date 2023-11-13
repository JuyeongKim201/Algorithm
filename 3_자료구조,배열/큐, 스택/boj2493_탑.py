# 문제: 탑 (골드 5)
'''
1. 입력이 한 줄로 주어지기 때문에, 일단 리스트를 입력 받음.
2. 0 -> N-1 방향 가면서 스택으로 역추적 (시간 초과)
    +) i번째 탑 기준으로 나보다 낮은 이전 탑들은 쓸모가 없음 -> stack에서 제거해주기
'''
import sys
input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))
prev = []
res = []

for i in range(N):    
    flag = True

    while prev: # prev가 빌 때까지
        if prev[-1][1] >= towers[i]: # 수신됐다면, 해당 top 기록
            res.append(prev[-1][0]+1)
            flag = False
            break
        else: # i번째 탑보다 작은 이전 탑들은 스택에서 제거
            prev.pop()

    # i번째 탑도 prev에 넣어주기
    prev.append([i, towers[i]])

    # i번째 탑보다 높은 탑이 없었다면
    if flag:
        res.append(0)
    

print(" ".join(map(str, res)))
