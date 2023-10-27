

'''
[바텀-업 (Bottom-Up) 방식]
바텀-업 방식은 반복문을 사용하여 작은 부분 문제부터 시작하여 큰 부분 문제를 해결하는 방식입니다. 
이 방식에서는 부분 문제의 해결책을 테이블에 저장하고, 이를 사용하여 큰 부분 문제의 해결책을 구합니다.
'''
# 바텀 업
def fibonacci(n):
    dp = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 피보나치 수열의 10번째 항 구하기
result = fibonacci(10)
print(result)  # 55



'''
[탑-다운 (Top-Down) 방식]
탑-다운 방식은 재귀를 사용하여 큰 문제를 작은 부분 문제로 나누고, 이를 해결하는 방식입니다. 
이 방식에서는 메모이제이션을 사용하여 이전에 계산한 부분 문제의 결과를 저장하고, 중복 계산을 방지합니다.
'''


# 탑 다운 (dict)
def fibonacci(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

# 피보나치 수열의 10번째 항 구하기
result = fibonacci(10)
print(result)  # 55

