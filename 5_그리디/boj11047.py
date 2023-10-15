# 문제: 동전 0 
# (A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수) 조건 때문에 그리디 알고리즘 적용 가능
import sys
input = sys.stdin.readline

N, K = map(int,input().split())
Coins = []
cnt = 0

for i in range(N):
    Coins.append(int(input()))

Coins.sort(reverse=True)

while K > 0:
    for i in range(N):
        if K >= Coins[i]:
            times = K // Coins[i]
            K = K - Coins[i]*times            
            cnt = cnt + times

print(cnt)


