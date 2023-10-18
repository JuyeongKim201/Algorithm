# 문제: 안전영역 (실버 1)

'''
영역의 개수를 세는 것이 핵심


'''


import sys
sys.setrecursionlimit(10**6)

N = int(input())
land = []
for i in range(N):
    land.append(list(map(int,input().split())))


