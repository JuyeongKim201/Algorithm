# 문제: 소형기관차
'''
객차 1대를 끌어야할 수도 있음. 
    - ex) 35 40 50 10 100 45 60 인 경우

DP 접근
    - 2차원 배열로 태뷸레이션 수행한다는 아이디어



'''
import sys
input = sys.stdin.readline

n = int(input())
train = list(map(int, input().split()))
limit = int(input())

