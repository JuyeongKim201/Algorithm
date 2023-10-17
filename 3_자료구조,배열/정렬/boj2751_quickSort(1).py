# 퀵 소트 구현해보기 1
# 서브 리스트로 나누어 구현 
'''
이해를 위한 쉬운 ver. 
재귀 개념을 더 적극 활용하였고, 퀵 소트의 개념 이해에 도움이 되는 코드이다. 
'''


nums = []
for i in range(int(input())):
    nums.append(int(input()))

def quick_sort(nums):
    # base case: 리스트 길이가 1 이하가 되면 더 이상 정렬할 게 없으므로 return
    if len(nums) <= 1:
        return nums
    
    # pivot 선택 - 가운데 인덱스를 기준으로 하는 이유: 최악의 경우(이미 정렬된 리스트)에 더 안정적인 성능
    pivot = nums[len(nums)//2]

    # 분할하기
    left, mid, right = [], [], []
    for num in nums: # nums의 요소들을 훑으면서 pivot을 기준으로 분류
        if num < pivot: 
            left.append(num)
        elif num > pivot:
            right.append(num)
        else:
            mid.append(num)

    # 재귀적으로 left, right 서브 리스트를 정렬한 후, 병합
    return quick_sort(left) + mid + quick_sort(right)


nums = quick_sort(nums)
for num in nums:
    print(num)

