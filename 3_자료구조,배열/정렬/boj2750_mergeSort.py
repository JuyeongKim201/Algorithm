# 머지 소트 구현해보기

'''
1. 분할 (Divide): 주어진 배열을 가장 작은 부분 배열이 될 때까지 반으로 계속 나눈다. 
    즉, 부분 배열의 원소가 0개 혹은 1개가 되면 1번 과정은 끝나고 2번으로 넘어간다. 

2. 정복(Conquer): 각 부분 배열을 재귀적으로 병합 정렬한다.
-> 가장 작은 부분 배열부터 '3. 병합 (Merge)' 과정을 수행하며 최초 크기의 배열까지 올라온다. 

3. 병합 (Merge): 양쪽의 배열(left, right)을 정렬하면서 합친다. 
'''

# Merge Sort 전체를 수행하는 함수
def merge_sort(arr):
    # base case: 배열의 길이가 1 이하라면 반환
    if len(arr) <= 1:
        return arr
    
    # 1. 분할 (Divide) - 가운데 인덱스를 기준으로 양분하기    
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    
    # 2. 정복
    left = merge_sort(left)
    right = merge_sort(right)

    # 3. 결합: 두 부분 배열을 merge
    return merge(left, right)
    

# Merge Sort 내부의 '3. 병합' 과정을 수행하는 함수
def merge(left, right):
    result = []
    i = j = 0 # i와 j는 각각 left와 right 배열의 인덱스

    # left와 right의 원소를 비교하며 result에 추가
    while i < len(left) and j < len(right): # 둘 중 하나가 빌 때까지
        # 더 작은 순서대로 임시 배열(result)에 담기
        if left[i] < right[j]:
            result.append(left[i])
            i += 1 # 다음 인덱스로 이동
        else:
            result.append(right[j])
            j += 1 # 다음 인덱스로 이동

    # 남아 있는 원소들을 순서대로 result에 추가
    '''
    이때, left에 원소가 남았든 right에 남았든, 남아 있는 원소들은 반드시 result의 가장 큰 값보다 크다. 
    '''
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1

    return result





### 문제 입력받는 부분 ###
arr = []
for i in range(int(input())):
    arr.append(int(input()))

### 문제 출력하는 부분 ### 
arr = merge_sort(arr)
for num in arr:
    print(num)


