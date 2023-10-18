# 문제: 수 찾기 (실버 4)
# 이분 탐색 구현해보기
'''
단순한 상황에서 이분 탐색을 구현할 때는 굳이 재귀로 들어갈 필요없음.
인덱스를 이용해 매번 탐색 범위를 반으로 줄여나가면 된다.
이 문제의 경우, 재귀 접근 대신 인덱스를 활용하면 공간 복잡도에서 이득을 보고, 실행 시간 측면에서 약간의 이득을 본다.
'''

import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))


# binary search
def binarySearch(list, n):
    start = 0
    end = len(list)-1

    while start <= end: # 인덱스가 1개라도 있으면
        mid = (start+end)//2
        if n == list[mid]:
            return 1
        elif n < list[mid]:
            end = mid - 1
        else:
            start = mid + 1
    
    # 어디에도 해당하지 않으면 해당 요소가 없는 것
    return 0
        
A.sort()    
for m in M_list:
    print(binarySearch(A, m))



