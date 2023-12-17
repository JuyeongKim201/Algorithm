# 문제: 내일로 여행 (골드 3)
'''
1. M_cities 순회 최저비용 구하기
2. 내일로 순회 최저비용 구하기
    1) 타입 = Mugunghwa, ITX-Saemaeul, ITX-Cheongchun 은 무료
    2) 타입 = S-Train, V-Train 은 cost를 절반으로
    3) 1과 동일하게 최저비용 구하기
    4) 내일로 티켓값 더하기
3. 1번값과 2번값 비교

최단거리 순회 어떻게 하더라
'''
N, naeil_p = map(int, input().split())
N_cities = list(map(str, input().split()))
M = int(input())
M_cities = list(map(str, input().split()))
K = int(input())

# 대중교통 테이블
graph = []
graph_naeil = []
for i in range(K):
    type_, s, e, cost = map(str, input().split())
    graph.append([type_, s, e, int(cost)])

    if type_ == 'Mugunghwa' or type_ == 'ITX-Saemaeul' or type_ == 'ITX-Cheongchun':        
        graph_naeil.append([type_, s, e, 0])
    elif type_ == 'S-Train' or type_ == 'V-Train':
        graph_naeil.append([type_, s, e, int(cost)/2])    
    else:        
        graph_naeil.append([type_, s, e, int(cost)])

# 방문여부 체크
visited = {}
for city in M_cities:
    visited[city] = False




