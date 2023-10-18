# 문제: 곱셈 (실버 1)
'''
거듭제곱의 나머지 성질

(A*B)%C = [(A%C) * (B%C)]%C

- B == 11일 때
(A^11)%C
    = [(A^5)%C * (A^5)%C]%C 

- B == 8일 때
(A^8)%C 
    = [(A^4)%C * (A^4)%C]%C 
    = {[(A^2)%C * (A^2)%C] * [(A^2)%C * (A^2)%C]}%C
    = ..

- B == 3일 때
(A^3)%C
    = [(A%C) * ((A^2)%C)]%C
    = {(A%C) * {[(A%C) * (A%C)]%C}%C

'''
import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

def remain(A, n):
    if n == 1:
        return A%C
    else:
        part = remain(A, n//2)
        if n % 2 ==0:
            return (part * part) % C
        else:
            return (part  * part * A) % C
          
print(remain(A, B))


