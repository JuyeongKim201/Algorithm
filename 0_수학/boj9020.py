# 문제: 골드바흐의 추측 (실버 2)
# 풀이 시간복잡도: O(n^2)

# 1. 소수 리스트 만들기
primeNumbers = []

for i in range(2, 10001):
    isPrime = True
    for j in range(2, i):
        if i%j == 0:
            isPrime = False
            break
    
    if isPrime:
        primeNumbers.append(i)


# 2. 골드바흐 파티션 추출
T = int(input())

for _ in range(T):
    n = int(input())
    partitians = []

    for i in primeNumbers:
        escape = False # 탈출 조건

        if i > n: # n보다 큰 소수는 검사 x
            break

        sample = n-i

        for j in primeNumbers:
            if j > i: # 파티션 중복 카운트 방지
                escape = True # 탈출
                break

            if i+j == n: # 파티션 조건 만족
                partitians.append([j, i])

            
    if len(partitians) == 1:
        print(partitians[0][0],partitians[0][1])
        
    else:
        minDiff = 10000
        minDiffPartitian = []

        for partitian in partitians:
            diff = partitian[1] - partitian[0]
            if diff < minDiff:
                minDiff = diff
                minDiffPartitian = partitian
        
        print(minDiffPartitian[0],minDiffPartitian[1])

