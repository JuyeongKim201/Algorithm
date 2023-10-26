'''
위상정렬
    - DAG (사이클이 없는 방향 그래프에서 가능)
    - indegree 만들기 (visited는 필요X)
    - 그래프 만들기. 이때 indegree도 함께 채워줌
    - 큐 활용 (bfs와 원리 비슷함)
    - 시작 (while문 전에) 
        indegree 0인 애들 모두 담기
    - while 문 안
        큐에서 꺼내서 방문
        인접노드 indegree -1
        새롭게 indegree 0된 애들 큐에 담기
    
'''

