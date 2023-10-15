# 문제: 팩토리얼 (브론즈 5)

N = int(input())

def fact(N):
    # base condition
    if N == 0: 
        return 1
    # general condition
    else:
        return N * fact(N-1)

result = fact(N)
print(result)

