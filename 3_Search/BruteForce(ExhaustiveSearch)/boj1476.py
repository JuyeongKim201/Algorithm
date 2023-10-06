# 문제: 날짜 계산 (백준 1476, 실버5)

tE, tS, tM = 1, 1, 1
year = 1

E, S, M = map(int, input().split())

while True:
    # 연도 조정
    if tE == 16:
        tE = 1
    if tS == 29:
        tS = 1
    if tM == 20:
        tM = 1

    if (tE == E) & (tS == S) & (tM == M):
        break
    
    # 연도 추가
    tE += 1
    tS += 1
    tM += 1

    year += 1

print(year)


