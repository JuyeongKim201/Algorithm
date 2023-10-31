'''
yeshowmuchiloveyoumydearmotherreallyicannotbelieveit
yeaphowmuchiloveyoumydearmother
'''


def lcs(str1, str2):
    dp = [[] for i in range(len(str1)+1)]
    
    for i in dp: 
        for j in range(len(str2)+1):
            i.append(0)
        
    traceBack = [list(i) for i in dp]
        

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1 
                traceBack[i][j] = 'left_up' # 좌상에서 내려옴
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    dp[i][j] = dp[i-1][j]
                    traceBack[i][j] = 'up' # 위로
                elif dp[i-1][j] <= dp[i][j-1]:
                    dp[i][j] = dp[i][j-1]
                    traceBack[i][j] = 'left' # 왼쪽으로

    # 문자열 추출하기
    i, j = len(str1), len(str2)
    lcs_str = ''
    while i > 0 and j > 0:
        if traceBack[i][j] == 'left_up':
            lcs_str = str1[i-1]+lcs_str # 해당 문자열 넣기
            i -= 1
            j -= 1
        elif traceBack[i][j] == 'up':
            i -= 1
        else:
            j -= 1
    

    return dp[len(str1)][len(str2)], lcs_str



str1 = input()
str2 = input()

lcs_value, lcs_str = lcs(str1,str2)
print(lcs_value)
print(lcs_str)



