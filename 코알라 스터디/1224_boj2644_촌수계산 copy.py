# 문제: 촌수계산 (실버 2)
'''
1. 각 노드가 부모 정보, 자식들 정보 담고 있도록 세팅
2. 촌수 계산: 
    1. 한쪽 노드에서 부모 노드 끝까지 타고 올라가기 (count 세기)
    2. 해당 조상 노드가 탐색할 노드인지 체크 
    3. 해당 조상 노드에서 dfs로 타겟 자식 찾기
        - 찾으면 return count 한 다음 위 count랑 더하기
        - 못 찾으면 return -1
'''
import sys
input = sys.stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())

relation = {i: [False, []] for i in range(1, n+1)}

for i in range(m):
    x, y = map(int, input().split())
    relation[x][1].append(y) # x의 자식 추가
    relation[y][0] = x # y의 부모 설정


def find_up(a, count):
    if not relation[a][0]:
        return [a, count]
    
    parent = relation[a][0]
    print(f'{a}의 parent: {parent}')
    find_up(parent, count+1)


def find_down(start, target, count):
    if start == target:
        return count        
    
    childs = relation[start][1]

    if not childs: # 자식이 더 이상 없는 경우
        return -1

    for child in childs:
        find_down(child, target, count+1)
        return


print(find_up(a, 0))
# root, count_up = up_result[0], up_result[1]
# print(up_result)
# count_down = find_down(root, b, 0)
# if count_down == -1:
#     print(-1)
# else:
#     print(count_up + count_down)
    



