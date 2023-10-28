# 문제: 동전 (골드 5)
'''
coins = [a,b,c,...] // M = n 일 때
점화식: dp[n] = dp[n-a] + dp[n-b] + dp[n-c] .. 

점화식 접근보다는 모든 금액을 만들어본다는 마인드로 접근
각 동전 단위를 사용하여 가능한 모든 금액을 만들어보고, 그 과정에서 중복 계산을 피하기 위해 이전에 계산한 결과를 재사용
'''

def count(coins, M):
    # dp[i] = 금액 i를 만들 수 있는 방법의 수
    dp = [0 for _ in range(M + 1)]
    dp[0] = 1  # 금액 0을 만드는 방법도 저장해야 DP가 동작함 (0 만드는 법 = 아무것도 안넣기 한 개)

    for coin in coins:
        for n in range(coin, M + 1):
            dp[n] += dp[n - coin]  # 현재 동전을 사용하여 금액 n를 만드는 방법의 수를 업데이트            

    return dp[n]


### 입출력 부분 ###
T = int(input())

for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    
    print(count(coins, M))
    
