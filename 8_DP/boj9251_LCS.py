'''
[기본 아이디어]
문자열 A, B가 주어졌을 때, (i = index)
CS 배열을 만듦 -> CS = [0]*(number of i)

if A[i] == B[i]:
    if i == 0:
        CS[i] = 1
    else:
        CS[i] = CS[i-1] + 1
ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
문제는 두 문자열의 길이, 공통 부분 배열의 위치가 다를 수도 있음.

일치하는 순간 재귀로 들어가서 쭉 탐색하는 건 어떨지? 
'''


A = input()
B = input()

na, nb = len(A), len(B)

# 더 긴 문자열 기준으로 세팅
CS = [0]*max(na, nb)

if A[0] == B[0]:
    CS[0] = 1

save_i = 0
save_j = 0
for i in range(na):
    for j in range(save_j, nb):
        if A[i] == B[j]:
            CS[i] = CS[save_i] + 1
            save_i = i
            save_j = j+1
            break

print(max(CS))



