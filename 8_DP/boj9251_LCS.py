# 문제: LCS (골드 5)
'''
각 i와 j에 대해서, dp[i][j]는 str1과 str2 전체의 LCS를 구하는 것의 하위 부분 문제들, 
즉 str1[i-1]와 str2[j-1]의 LCS를 구하는 문제인 셈. 

dp[i][j]에는 각 부분 문제들의 답을 기록해놓는 거고, 
각 문자열의 다음 문자로 넘어가면 이전 문제의 답에서 시작해서 한 문자만 추가하면 되는 것.

str1[i] == str2[j-1]일 때 대각선 위에서 +1을 해주는 이유는
하위 문제를 점차 확장해나간다는 아이디어에선, 
현재 상황이 양쪽 문자열에서 한 글자씩 빠진 상황에서의 답에
양쪽 문자열에 현재 문자들 하나씩만 추가된 상황이나 마찬가지이기 때문. 
--------------------
--------------------
import sys로 문자열을 받으면 마지막 '\n'까지 문자열의 일부로 치는듯
그래서 카운트가 한 개 더 된다. 

시간적으로도 그냥 input()으로 받는게 더 빨라서 빼는게 낫다. 
'''

def lcs(str1, str2):
    dp = [[] for i in range(len(str1)+1)]
    for i in dp:
        for j in range(len(str2) + 1): 
            i.append(0)

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # 현재 양쪽 문자가 일치하는 경우
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1 # LCS 업데이트 (대각선 위의 값 + 1)

            # 문자가 일치하지 않는 경우
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # 왼쪽, 위쪽 중에 큰 값 물려받기

    return dp[len(str1)][len(str2)]


### I/O ### 
str1 = input()
str2 = input()

print(lcs(str1, str2))


