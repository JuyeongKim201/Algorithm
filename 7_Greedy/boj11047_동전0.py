# 문제: 동전 0 (실버 4)
'''
- 탐욕적 선택 조건: K원을 만들기 위해 가능한 한 가치가 큰 동전을 먼저 선택한다.
- 최적 부분 구조: K == 4200이라면, 1000원 갯수를 구하는 단계

'''
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = []
for i in range(N):
    coin = int(input())
    if coin <= K:
        A.append(coin)

A.sort(reverse=True)

cnt = 0

for coin in A:
    if K == 0:
        break

    x = K//coin
    K -= coin*x
    cnt += x

print(cnt)            






