# 문제: 차이를 최대로 (실버2)
# itertools.permutations() 활용해서 조합 뽑아낸 뒤, 전체 비교? - x

# 1) 양수 + 음수끼리 먼저 붙인다. 양수 + 음수 조합이면 수의 크기는 고려할 필요 없음. (결국 합쳐짐)
# 2) 양수 + 양수, 음수 + 음수라면, 고를 수 있는 최솟값과 최댓값 우선으로 붙인다. 

N = int(input())
numList = list(map(int,input().split()))

### 양수 그룹, 음수 그룹 나누기 ###
plus, minus = [], []
for i in numList:
    if i >= 0: plus.append(i)
    else: minus.append(i)

### 식의 최댓값 구하기 ### 
max = 0

used = [False for i in range(N)]

# only 양수일 때
if len(plus) > 0 and len(minus) == 0:
    for i in range(N):
        
# only 음수일 때
elif len(plus) == 0 and len(minus) > 0:
    print(1)
# 양수, 음수 둘 다 있을 때
else:
    print(1)









