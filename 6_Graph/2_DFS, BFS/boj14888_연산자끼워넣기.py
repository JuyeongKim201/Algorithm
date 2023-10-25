# 문제: 연산자 끼워넣기 (실버 1)
'''
순서를 바꾸면 안되는 수열

연산자를 하나씩 껴보면서 모든 경우의 수 탐색
    - 탐색 코드를 어떻게 설계할 것인가?
        주어진 연산자 숫자를 하나씩 소모하면서 가는 방법?
    - 중복되는 연산을 어떻게 제외할 것인가?

일단 문자 조합으로 ㄱㄱ
    - 모든 식이 완성되면 그때 계산해야 함
    - 문자를 계산으로 해석하는 코드 따로 필요
    
일단 dfs 탐색되는지 테스트 -> 마지막에 최댓값 최솟값 비교 추가하기

'''
import sys
from itertools import *
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


N = int(input())
nums = list(map(int, input().split()))
oper_num = list(map(int, input().split())) # +, -, *, / 순

oper_tmp = ['+']*oper_num[0]+['-']*oper_num[1]+['x']*oper_num[2]+['/']*oper_num[3]

# 사칙연산 조합 뽑아내기
# 여기서 시간복잡도 많이 먹음
operand = []
for i in permutations(oper_tmp, N-1):
    if i not in operand:
        operand.append(i)
        
min = 1e9+1
max = -1e9-1

leng = len(nums)
for oper in operand:
    # 각 문자열 완성
    oper += ('','')
    string = ''    
    for i in range(len(nums)):
        string += str(nums[i])+oper[i]
    
    # 실제 값으로 바꾸기 
    


    # 최대 최소 비교하기




