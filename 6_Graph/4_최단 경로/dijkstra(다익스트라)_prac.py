'''
[다익스트라 알고리즘의 핵심 아이디어]

다익스트라 알고리즘은 시작 노드로부터 모든 다른 노드까지의 최단 경로를 찾는 알고리즘이며, 
이는 "탐욕적 방법(Greedy Method)"을 사용합니다. 
알고리즘은 시작 노드의 거리를 0으로 설정하고, 나머지 모든 노드의 거리를 무한대로 설정합니다. 
그리고 알고리즘은 현재 노드에서 이웃하는 노드들의 거리를 업데이트하며, 
미방문 노드 중에서 거리가 가장 작은 노드를 선택하여 그래프를 탐색합니다.
----------------------------------
[구현 방법의 핵심 요약] (시각화: https://www.cs.usfca.edu/~galles/visualization/Dijkstra.html)

- 시작 노드를 설정하고, 모든 노드의 거리를 무한대로 초기화합니다.
- 우선순위 큐를 사용하여 미방문 노드 중 거리가 가장 작은 노드를 선택합니다.
- 선택된 노드의 이웃 노드들의 거리를 업데이트합니다.
- 모든 노드를 방문할 때까지 위의 과정을 반복합니다.
----------------------------------
우선순위 큐에는 (cost, 노드) 순으로 넣어야 한다.

heapq.heappop() 함수를 호출할 때, 힙에서 가장 작은 요소가 팝되며, 이 요소는 튜플의 첫 번째 요소를 기준으로 정렬됩니다. 
따라서 heappop()을 사용하여 비용을 기준으로 요소를 팝하려면, 튜플의 첫 번째 요소로 비용을 지정하고 두 번째 요소로 노드를 지정해야 합니다.

'''
import heapq

def dijkstra(graph, start, end):
    # 거리를 저장할 딕셔너리 초기화, 시작 노드의 거리는 0, 나머지 노드의 거리는 무한대로 설정
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # 우선순위 큐 초기화
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  # (거리, 노드) 튜플 형태로 저장

    while priority_queue:
        # 현재 노드와 현재 노드까지의 거리를 가져옴
        print(priority_queue)
        current_distance, current_node = heapq.heappop(priority_queue)

        # 이미 처리된 노드는 무시
        if distances[current_node] < current_distance:
            print(f'{current_node}는 이미 확정됨. ({current_distance}, {current_node}) 무시!')
            continue

        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight
            # 인접 노드까지의 거리가 더 짧은 경우 업데이트
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(priority_queue, (distance, adjacent))  # 업데이트된 거리와 인접 노드를 큐에 추가

    return distances[end]

# 가상의 그래프를 인접 리스트 형태로 정의
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# 출발 노드 'A'에서 도착 노드 'D'까지의 최단 거리 출력
print(dijkstra(graph, 'A', 'D'))  # Output: 4
