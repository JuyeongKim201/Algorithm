# 문제: 소수 찾기 (브론즈 2)

N = int(input())
numList = list(map(int,input().split()))
cnt = 0
for i in range(N):
    testNumber = numList[i]
    isPrime = True

    if testNumber == 1:
        continue
    
    for j in range(2, testNumber):
        if testNumber % j == 0:
            isPrime = False
            break

    if isPrime:
        cnt += 1

print(cnt)



