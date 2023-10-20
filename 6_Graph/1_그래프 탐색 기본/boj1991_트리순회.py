# 문제: 트리 순회 (실버 1)
# 딕셔너리로 트리 구현

'''
다음 구조를 통해 딕셔너리로 트리를 구현할 수 있다.

BT = {
    'A':['B','C'],
    'B':['D','.']
    }

# A의 왼쪽 노드 
left_node = BT['A'][0]

# A의 오른쪽 노드
right_node = BT['A'][1]
'''

def preorder(node):
    if node != '.':
        left_node, right_node = BT[node][0], BT[node][1]
        print(node, end='') # 해당 노드 스캔
        preorder(left_node) # 왼쪽 서브트리 스캔
        preorder(right_node) # 오른쪽 서브트리 스캔

def inorder(node):
    if node != '.':
        left_node, right_node = BT[node][0], BT[node][1]
        inorder(left_node) # 왼쪽 서브트리 스캔
        print(node, end='') # 해당 노드 스캔
        inorder(right_node) # 오른쪽 서브트리 스캔

def postorder(node):
    if node != '.':
        left_node, right_node = BT[node][0], BT[node][1]
        postorder(left_node) # 왼쪽 서브트리 스캔
        postorder(right_node) # 오른쪽 서브트리 스캔
        print(node, end='') # 해당 노드 스캔


### 입력 부분 ###

# 트리를 딕셔너리로 구현
BT = {}
for i in range(int(input())):
    parent, left_node, right_node = map(str,input().split())
    BT[parent] = [left_node, right_node]


### 출력 부분 ###
preorder('A')
print()
inorder('A')
print()
postorder('A')




