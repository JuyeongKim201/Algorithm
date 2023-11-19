# 문제: 소형기관차
'''
길이가 n개인 배열 train을 length 길이의 연속된 배열 3개로 나누는 문제
이때 모든 배열의 합은 최대가 되어야 함

1. 그리디 느낌 접근?? -> X
첫번째 기관차가 끝까지 탐색 -> 가장 큰 연속 배열 2개를 가져감 (2개는 0으로)
-> 두번째 기관차가 끝까지 탐색 -> ..

2. 분할정복??
'''
import sys
input = sys.stdin.readline

n = int(input())
train = list(map(int, input().split()))
length = int(input())
guest = 0

for _ in range(3):
    print(f'{_}호차 출발')
    head = 0
    maximum = 0
    max_start = 0
    for i in range(n-length+1):
        head = sum(train[i:i+length])
        print(f'{i}번째: {head}')
        if head >= maximum:
            maximum = head
            max_start = i
            print(f'maximum: {maximum}, max_start: {max_start}')            
    
    for j in range(max_start, max_start+length):
        train[j] = 0
    
    guest += maximum
    print(f'현재 객차 현황: {train}')
    print('----------------')


print(guest)



