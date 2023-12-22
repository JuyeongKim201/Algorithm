# 문제: 포도주 시식 (실버 1)
'''
f(n) = max (f(n-3) + dp[n-1] + dp[n], 
            f(n-2) + dp[n], 
            f(n-1))
'''
import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 0]
for i in range(n):
    dp.append(int(input()))

result = [0] * (n+2)
result[2] = dp[2]

if n == 1:
    print(result[2])
else:
    for i in range(3, len(result)):
        result[i] = max(result[i-3]+dp[i-1]+dp[i],
                        result[i-2]+dp[i], result[i-1])

    print(result[i])
