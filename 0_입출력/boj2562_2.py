# 최댓값 (브론즈 3)
# 메서드를 활용한 풀이 - max(), index()

numList = []
for i in range(9):
    num = int(input())
    numList.append(num)

print(max(numList))
print(numList.index(max(numList))+1)

