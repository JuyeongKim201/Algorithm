# 문제: 신입사원 (실버 1)
'''
서류심사, 면접시험 둘 다 다른 참가자 대비 딸리는 애는 안 뽑는다. 
만약 1 1 인 애가 뽑힌다면 한 명밖에 못 뽑음 
---------------------
엇갈릴수록 좋음
---------------------
1. 등수 차이가 큰 순서 -> 작은 순서로 정렬 
2. 서류심사 or 면접시험 점수 중 하나를 두번째 기준으로 써서 정렬 
3. 둘 중 더 많이 뽑을 수 있는 거 기준으로 선발

'''
import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    mens = []
    N = int(input())
    for i in range(N):
        resume, interview = list(map(int, input().split()))
        mens.append([resume, interview, interview-resume])

    # mens.sort(key = lambda x: (-abs(x[2]), -x[1])) # 등수 차이를 1, 서류 등수를 2번째 기준으로 내림차순 정렬    
    # interview_cutline = 100001

    # cnt = 0 # 합격자 수
    # passmen = []

    # print(mens)

    # for i in mens:
    #     if i[1] < interview_cutline: 
    #         cnt += 1
    #         passmen.append(i)                        
    #         interview_cutline = i[1]
    
    # print(_, "회차 합격: ", passmen, cnt)
    
    mens.sort(key = lambda x: (-abs(x[2]), -x[2])) # 등수 차이를 1, 면접 등수를 2번째 기준으로 내림차순 정렬
    resume_cutline = 100001
    
    cnt = 0 # 합격자 수
    passmen = []

    print(mens)

    for i in mens:
        if i[1] < resume_cutline: 
            cnt += 1
            passmen.append(i)                        
            resume_cutline = i[1]
    print(_, "회차 합격: ", passmen, cnt)

    
            
    



