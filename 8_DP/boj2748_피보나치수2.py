# 문제: 피보나치 수2 (브론즈 1)
'''
점화식: f(n) = f(n-1) + f(n-2)
바텀 업, 탑 다운 한번씩 구현해보기

바텀 업: 테이블 - 반복문 사용
탑 다운: 메모이제이션 - 재귀, dict
'''

# 바텀 업
def fibo1(n):
    table = [0, 1] + [0]*90
    if n <= 1:
        return table[n]

    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]

    return table[n]

# 탑 다운 (dict)
def fibo2(n, memo = {}):
    if n <= 1:
        return n
    
    if n not in memo:
        memo[n] = fibo2(n-1, memo) + fibo2(n-2, memo)
    
    return memo[n]

n = int(input())
print(fibo1(n))
print(fibo2(n))



