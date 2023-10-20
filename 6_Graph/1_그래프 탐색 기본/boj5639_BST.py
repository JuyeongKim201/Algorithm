# 문제: 이진 검색 트리 (골드 5)

'''
비선형 자료구조 -> (전위 순회) -> 선형으로 결과값들 출력 

결과값들의 구조는 다음과 같다.
[[Root],[왼쪽 Subtree],[오른쪽 Subtree]] <- 재귀

------ 구현 ------
0. 입력값 받아서 output을 리스트 형태로 만들기
1. 결과값을 토대로 역으로 BST 구성
2. 구성된 BST를 postorder 순회 후 출력
-----------------
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 1. preorder 결과값을 토대로 BST 구성
def make_BST(output):
    # 리프 노드 혹은 빈 노드가 들어왔을 경우     
    if len(output) == 1:
        root = output[0]
        BST[root]=['.', '.']
        return
    elif len(output) == 0:
        return
    
    # 자식을 가진 노드가 들어왔을 경우
    root = output[0]
    left, right = [], []
    
    # 왼쪽, 오른쪽 subtree 나눠주기
    for node in output:
        if node < root:
            left.append(node)
        elif node > root:
            right.append(node)

    # 노드 추가하기: 길이가 1이 아니라면 왼쪽 or 오른쪽 subtree 중 하나는 반드시 존재함
    if len(left) == 0:
        BST[root]=['.', right[0]]
    elif len(right) == 0:
        BST[root]=[left[0], '.']
    else: 
        BST[root]=[left[0], right[0]]

    make_BST(left)
    make_BST(right)


# 2. BST를 postorder 순회
def postorder(node):
    if node != '.': # 빈 노드가 아니라면
        left, right = BST[node][0], BST[node][1]

        # 리프 노드일 때는 리턴
        if left == '.' and right == '.': 
            print(node)
            return
        
        postorder(left) # 왼쪽 subtree 순회
        postorder(right) # 오른쪽 subtree 순회
        print(node) # 루트 노드 출력


### 입력 부분 ###
output = []
while True: # 입력이 끝날 때까지 받기
    try:
        output.append(int(input()))
    except:
        break

BST = {}
make_BST(output)
print(BST)
# postorder(output[0]) # 전위 순회의 출력값에선 0번째 index가 root 노드


