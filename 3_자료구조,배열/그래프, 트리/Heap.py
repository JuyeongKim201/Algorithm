########## heapq 모듈을 활용한 Heap 자료구조 구현  ##########
import heapq

#------ 최소 힙 ------#
min_heap = []

# 삽입
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 7)
print(min_heap)  # 결과: [3, 5, 7]

# 최소값 검색
min_value = min_heap[0]  # 루트 노드 조회
print(min_value)  # 결과: 3

# 삭제
min_value = heapq.heappop(min_heap)  # 루트 노드(최소값) 삭제 및 반환
print(min_value)  # 결과: 3
print(min_heap)  # 결과: [5, 7]




#------ 최대 힙 ------#
max_heap = []

# 삽입
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -7)
print([-i for i in max_heap])  # 결과: [7, 3, 5]

# 최대값 검색
max_value = -max_heap[0]  # 루트 노드 조회
print(max_value)  # 결과: 7

# 삭제
max_value = -heapq.heappop(max_heap)  # 루트 노드(최대값) 삭제 및 반환
print(max_value)  # 결과: 7
print([-i for i in max_heap])  # 결과: [5, 3]



########## 모듈 내부 동작 구현 ##########
# heap 배열 정의
heap = []

# 삽입 연산
def insert(heap, value):
    # Heapify up
    heap.append(value)  # 요소를 배열의 마지막에 삽입
    index = len(heap) - 1  # 새로 삽입된 요소의 인덱스 배정
    while index > 0:  # 루트 노드에 도달할 때까지 또는 힙 속성이 유지될 때까지 반복
        parent_index = (index - 1) // 2  # 부모 노드의 인덱스 계산
        if heap[index] < heap[parent_index]:  # 최소 힙의 경우, 새 노드가 부모 노드보다 작으면
            heap[index], heap[parent_index] = heap[parent_index], heap[index]  # 새 노드와 부모 노드의 위치를 바꿈
            index = parent_index  # 새 노드의 인덱스를 부모 노드의 인덱스로 업데이트
        else:
            break  # 힙 속성이 유지되면 종료

# 삭제 연산
def delete(heap):
    if not heap:
        return None  # 힙이 비어있으면 None 반환
    root = heap[0]  # 루트 노드의 값 저장
    heap[0] = heap.pop()  # 배열의 마지막 요소를 루트로 이동
    index = 0
    while index * 2 + 1 < len(heap):  # 왼쪽 자식 노드가 존재하는 동안 반복
        child_index = index * 2 + 1  # 왼쪽 자식 노드의 인덱스 계산
        # 오른쪽 자식 노드와 비교 (최소 힙의 경우)
        if child_index + 1 < len(heap) and heap[child_index] > heap[child_index + 1]:
            child_index += 1  # 오른쪽 자식 노드가 더 작으면 오른쪽 자식 노드를 선택
        if heap[index] > heap[child_index]:  # 현재 노드가 선택된 자식 노드보다 크면
            heap[index], heap[child_index] = heap[child_index], heap[index]  # 현재 노드와 자식 노드의 위치를 바꿈
            index = child_index  # 현재 노드의 인덱스를 자식 노드의 인덱스로 업데이트
        else:
            break  # 힙 속성이 유지되면 종료
    return root  # 삭제된 루트 노드의 값 반환

# 검색(조회) 연산
def peek(heap):
    return heap[0] if heap else None  # 힙이 비어있지 않으면 루트 노드의 값 반환, 비어있으면 None 반환


