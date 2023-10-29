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

----
거의 다 왔는데 딕셔너리 삭제 논리가 완벽하지 않음. 완성 필요        
'''
from collections import defaultdict

def lcs(str1, str2):
    dp = defaultdict(int)
        
    lcs_value = 0

    # 딕셔너리 채우기 -> 최댓값 갱신되면 count, i값만 
    # 최장 문자열 -> str1[i] 부터 역으로 count만큼 뽑아내면 됨
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):

            # 현재 양쪽 문자가 일치하는 경우
            if str1[i-1] == str2[j-1]:
                dp[i,j] = dp[i-1, j-1] + 1 # LCS 업데이트 (대각선 위의 값 + 1)
                if dp[i, j] > lcs_value:
                    lcs_value = dp[i, j]
                    max_i = i
                
                
            # 문자가 일치하지 않는 경우
            else:
                dp[i, j] = 0

            if i > 2 and j > 2:
                del dp[i-2, j-2]


    # return lcs_value, lcs_string
    return lcs_value, max_i, dp


### I/O ### 
str1 = input()
str2 = input()


# lcs_value, lcs_string = lcs(str1, str2)

lcs_value, max_i, dp = lcs(str1, str2)
lcs_string = str1[max_i-lcs_value: max_i]

print(lcs_value)
print(lcs_string)

print(dp)