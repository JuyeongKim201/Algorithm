# 문제: 주사위 세개


def calculateReward(): 
    dices = list(map(int, input().split()))
    numbers = [1,2,3,4,5,6]
    reduplication = [0,0,0,0,0,0,0]

    # 1부터 6까지 각각 몇 개가 나왔는지 카운트
    for i in dices: 
        for number in numbers: 
            if i == number:
                reduplication[number] += 1
    
    # 최대 중복 개수 구하기
    value = 1
    maximum = reduplication[1]
    for i in range(2, 7):
        if reduplication[i] > maximum:
            maximum = reduplication[i]
            value = i    

    # 상금 계산
    if maximum == 3:
        reward = 10000 + (value * 1000)
        return reward
    
    elif maximum == 2:
        reward = 1000 + (value * 100)
        return reward

    elif maximum == 1:
        reward = max(dices) * 100
        return reward
            

print(calculateReward())

