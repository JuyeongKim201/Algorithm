# 문자열 반복 (브론즈 2)

T = int(input())

for i in range(T):
     R, S = map(str, input().split())
     P = ""
     for j in S:
        P += j*int(R)
     print(P)
