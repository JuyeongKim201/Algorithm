'''
<우선순위 큐>
우선순위 큐는 데이터를 추가한 순서대로 제거하는 선입선출(FIFO) 특성을 가진 일반적인 큐의 자료구조와 달리, 
데이터 추가는 어떤 순서로 해도 상관이 없지만, 제거될 때는 가장 작은 값을 제거하는 독특한 특성을 지닌 자료구조입니다. 
이 말은 내부적으로 데이터를 정렬된 상태로 보관하는 메커니즘이 있다는 뜻이고, 좀 더 구체적으로 얘기하면 heapq 모듈을 통해 구현되어 있습니다.
----------------------------------------

파이썬에서의 우선순위 큐 구현은 3가지 방법이 있음.
1. heapq 모듈 사용
    - 간단하고 효율적
2. queue.PriorityQueue 클래스 사용
    - thread-safe한 우선순위 큐 제공
3. sortedcontainers 라이브러리 사용
    - 높은 수준의 성능

일반적으로 heapq가 많이 쓰이는 거 같으니 그것부터 연습!

'''
import heapq

priority_que = []
for i in range(10):
    heapq.heappush(priority_que, i)
print(priority_que) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(3):
    a = heapq.heappop(priority_que)
    print(a)
print(priority_que) # [3, 4, 5, 7, 9, 8, 6]

heapq.heappushpop(priority_que, 99) # pop과 동시에 새로운 요소 push
print(priority_que) # [4, 7, 5, 99, 9, 8, 6]


'''
heapq 모듈은 리스트의 첫 번째 요소(인덱스 0)가 항상 힙의 최소값을 가지도록 유지합니다. 
그러나 나머지 요소들은 특정 순서로 정렬되지 않습니다. 대신 이들 요소는 힙 속성을 유지하기 위해 정렬됩니다. 
이는 heapq.heappop() 함수를 호출할 때마다 리스트의 첫 번째 요소가 최소값을 가지도록 보장하며, 
나머지 요소들은 힙 속성을 유지하도록 재정렬됩니다.
'''


