# 문제: 피보나치 수 (브론즈 2) - 재귀를 이용한 풀이

def fibo(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)
    
N = int(input())
print(fibo(N))

# for문을 활용한 풀이

N = int(input())
fibo = [0 for _ in range(50)]
fibo[1], fibo[2] = 1, 1
for i in range(3, 46):
    fibo[i] = fibo[i-2] + fibo[i-1]
    
print(fibo[N])

