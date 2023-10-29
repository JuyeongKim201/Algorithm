# 문제: 최장 공통 부분 문자열 (플레 3)
'''
LCS 문제와 거의 동일. 차이점은
    1. 부분 문자열은 원본 문자열 상에서 연속된 문자로 구성되어 있을 것 (중간에 끊기면 x)
    2. LCS 값뿐 아니라 LCS에 해당하는 문자열을 함께 출력할 것
(구현은 완료)
--------------
<메모리 초과!!> 
    - 문자열 길이가 합 20만으로 매우 길어진게 원인인듯. 최악의 경우를 2차원 배열로 만들면 공간복잡도가 너무 커짐
    -> 2차원 배열이 아니라 해시테이블 이용하면 어떨지? 
        - 키값: i, j 좌표를 튜플로 처리
        - 키값을 다 만들어놓는 것도 메모리 부담됨 -> defaultdict 사용
(이것도 메모리 초과)
--------------
dfs로 가면 시간초과 나려나
'''
from collections import defaultdict
import sys

def lcs(str1, str2):        
    max_count = 0
    max_string = ''
    tmp_count = 0
    tmp_string = ''

    # 테이블 채우기
    # LCS 값: tmp_count 저장 -> 
    # 문자열: tmp_string 저장 -> max 갱신되면 max_string을 tmp_string으로 대체
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # 현재 양쪽 문자가 일치하는 경우
            if str1[i-1] == str2[j-1]:
                tmp_count += 1 # 카운트 + 1
                tmp_string += str1[i-1] # 문자열 계속 기록하기
                print(tmp_string)
                
                # 만약 count가 최댓값이라면 최대 카운트, 문자열 업데이트
                if tmp_count > max_count:
                    max_count = tmp_count
                    max_string = tmp_string
            
            else: 
                tmp_count = 0
                tmp_string = ''
                                    
                    

    return max_count, max_string



## I/O ### 
str1 = input()
str2 = input()

lcs_value, lcs_string = lcs(str1, str2)
print(lcs_value)
print(lcs_string)



'''
str1 = ''
str2 = ''
for i in range(3000):
    str1 += 'a'
    str2 += 'a'

dp = lcs(str1, str2)
print(sys.getsizeof(dp)) // 3.3억 바이트 (3gb..?)
print(sys.getsizeof(str1)) // 3000
print(sys.getsizeof(str2)) // 3000

각 문자 길이를 3000씩만 해도 최악의 경우 이런 상황
해쉬테이블에서 여전히 많이 잡아먹음
'''