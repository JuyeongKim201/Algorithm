# 문제: 수 정렬하기 2
# 파이썬의 sort() 함수는 Timsort 알고리즘은 사용함
# Timsort 알고리즘은 merge sort와 insert sort를 혼합한 방식으로,
# 시간복잡도는 최선 = O(n)// 평균, 최악 = O(nlogn) 이다. 
# Merge sort 대비 최선의 경우 효율적, Quick sort 대비 최선 최악의 경우 모두 효율적이다. 
# 따라서 어지간한 정렬 알고리즘보다 내장 함수 sort()가 더 효율적이라는 뜻
import sys
input = sys.stdin.readline

N = int(input())
numList = []
for i in range(N):
    numList.append(int(input()))

numList.sort()
for i in numList:
    print(i)

