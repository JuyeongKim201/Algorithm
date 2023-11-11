# 문제: Z (실버 1)
'''
돌면서 카운트? -> print((2**15)*(2**15)) = 10억..

0 1
2 3
각각 시작점: 
    0*2^(2N-2)
    1*2^(2N-2)
    2*2^(2N-2)
    3*2^(2N-2)

r, c = 각각 2^N//2 기준으로 큰지 작은지에 따라서 0, 1, 2, 3 사분면 판단 -> 시작점 세팅
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N, r, c = map(int,input().split())

def dnq(y, x, n, start_num):
    std = (2**n)//2
    if (y, x) == (r, c):
        return start_num
    
    if r <= std and c <= std: # 파트 0
        dnq(y, x, std, start_num) 
    elif r <= std and c > std: # 파트 1
        dnq(y, x+std, std, start_num+1*(2**(2*n-2))) 
    elif r > std and c <= std: # 파트 3
        dnq(y+std, x, std, start_num+1*(2**(2*n-2))) 
    else: # 파트 4
        dnq(y+std, x+std, std, start_num+1*(3**(2*n-2))) 

a = dnq(0, 0, N, 0)
print(a)



