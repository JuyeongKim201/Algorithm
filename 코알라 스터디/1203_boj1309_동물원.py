# 문제: 동물원 (실버 1)
'''
[DP]

2*n 칸에 대한 경우의 수:

f(x) = [0] [L] [R]
f(1) = 1 1 1
f(2) = f(1) + 2 + 2 = 7
f(3) = f(2) + [f(2).0 + f(2).R] + [f(2).0 + f(2).L]
    = 7 + [ 3 + 2 ] + [ 3 + 2 ] = 17
f(4) = f(3) + [f(3).0 + f(3).R] + [f(3).0 + f(3).L]
    = 17 + [ 7 + 5 ] + [ 7 + 5 ] = 41

f(n) = f(n-1) + 2*[f(n-1.0)+f(n-1.L)]

f(n.0) = f(n-1) 
f(n.L) = f(n-1.0) + f(n-1.L)
        =  f(n-2) + f(n-1.L)

- 테이블 3개 필요: 1) 0개 두는 테이블 (f(n.0)) 
                2) L 또는 R에 두는 테이블 (f(n.L))
                3) 결과 테이블 f(n)

'''
import sys
input = sys.stdin.readline

n = int(input())

placement_zero = [0, 1, 3]
placement_left = [0, 1, 2]
result = [0, 3, 7]

if n == 1:
    print(3)
elif n == 2:
    print(7)
else:
    i = 3
    while (i <= n):
        res_zero = result[i-1]
        res_left = placement_zero[i-1] + placement_left[i-1]

        placement_zero.append(res_zero % 9901)
        placement_left.append(res_left % 9901)

        res = result[i-1] + 2*(placement_zero[i-1]+placement_left[i-1])
        result.append(res%9901)

        i += 1
    
    print(result[n])

