# 문제: 나무 자르기 (실버 2)

'''
[이분 탐색 활용한 풀이]

#1. H = 가장 작은 나무(start)와 가장 큰 나무(end)의 평균 키로 설정한다. 
#2. 해당 H에서 얻을 수 있는 나무의 양(get)을 M과 비교한다. 
    1. get < M 일 경우 더 낮은 범위에서 H 재탐색
    2. get > M일 경우 더 높은 범위에서 H 재탐색

-------------
[get == M일 때 반환하지 않는 이유]

해당 문제에서는 get == M인 H 값을 무조건 반환하는 게 아니라, 
이를 만족하는 H값 중 최댓값을 반환해야 하는 문제이다. 
따라서 get == M을 만족하더라도 계속 탐색을 진행해야 한다. 
--------------
[start가 아닌 end 값을 반환하는 이유]

이분 탐색의 종료 조건은 start가 end보다 큰 경우. 
이때 end는 마지막으로 조건을 만족하는 H 값이며, start는 그보다 1 더 큰 값이 된다.
--------------
'''

import sys
input = sys.stdin.readline

N, M = map(int,input().split())
trees = list(map(int, input().split()))

def getLog(trees, M):
    start = 0
    end = max(trees)

    while start <= end:
        H = (start+end)//2 # 처음 순서 나무와 끝 순서 나무의 평균
        
        # 현재 H 값에서 얻을 수 있는 나무의 양
        get = 0
        for tree in trees:
            if tree >= H:
                get += tree - H

        # get과 M 비교하여 H 조정      
        if get < M: # M보다 적게 얻었음
            end = H - 1 

        else: # M보다 많이 얻었음
            start = H + 1 # (H+1) ~ end에서 재탐색

    # short와 long이 역전되었을 때, 우리가 원하는 최적의 H값은 long 값이 됨 (long이 더 짧음)
    return end

trees.sort()
H = getLog(trees, M)
print(getLog(trees, M))
