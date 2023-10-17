# 퀵 소트 구현해보기 2
# 포인터 구현 

'''
더 효율적인 ver. 교과서에서 소개된 코드임.
앞선 코드 대비 장점은 인플레이스(in-place)로 분할을 수행한다는 점.
즉, 추가적인 메모리를 사용하지 않고 입력 리스트 내에서만 작업을 수행함. 
첫번째 코드와 달리 리스트를 새로 만드는 메모리가 소요되지 않음. 
'''

nums = []
for i in range(int(input())):
    nums.append(int(input()))

def quick_sort(nums, left, right):
    # 양쪽 포인터를 양 끝으로 설정
    pl, pr = left, right
    
    # pivot 선택 - 가운데 인덱스를 기준으로 하는 이유: 최악의 경우(이미 정렬된 리스트)에 더 안정적인 성능
    pivot = nums[(left + right) // 2] 
    
    # 분할하기
    while pl <= pr: # pl과 pr이 교차할 때까지 
        while nums[pl] < pivot: 
            pl += 1 # pl을 오른쪽으로 이동. 코드를 반복하다보면 pivot 보다 큰 값에서 포인터는 멈추게 된다. 
        while nums[pr] > pivot:
            pr -= 1 # pl을 왼쪽으로 이동. 코드를 반복하다보면 pivot 보다 작은 값에서 포인터는 멈추게 된다. 
        
        # 아직 교차하지 않았다면
        if pl <= pr: 
            nums[pl], nums[pr] = nums[pr], nums[pl] # 양쪽 값의 위치를 교환
            pl, pr = pl+1, pr-1

    if left < pr:
        quick_sort(nums, left, pr)
    if pl < right:
        quick_sort(nums, pl, right)


nums = quick_sort(nums)
for num in nums:
    print(num)

