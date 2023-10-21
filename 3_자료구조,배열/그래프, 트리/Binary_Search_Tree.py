'''
이진 탐색 트리를 파이썬으로 구현해보는 파일
'''

# 노드 객체
class Node:
    def __init__(self, key):
        self.value = key # 현재 노드의 값을 저장
        self.left = None # 왼쪽 자식 노드를 가리킴
        self.right = None # 오른쪽 자식 노드를 가리킴


# 삽입
def insert(root, key):
    # 현재 노드가 없으면(리프에 도달했다면) 새로운 노드 생성 후 반환
    if root is None:
        return Node(key)
    
    # 삽입하려는 값이 현재 노드의 값보다 작으면 -> 왼쪽 구역에 삽입
    if key < root.value:
        root.left = insert(root.left, key)
    # 삽입하려는 값이 현재 노드의 값보다 크면 -> 오른쪽 구역에 삽입
    else:
        root.right = insert(root.right, key)
    
    return root # 반환된 노드(root)가 상위 호출에서 왼쪽 or 오른쪽 자식으로 설정됨

# 탐색
def search(root, key):
    # 현재 노드가 없거나 찾는 값이라면 반환해준다.
    if root is None or root.value == key:
        return root
    
    # 찾는 값이 현재 노드의 값보다 크면 오른쪽으로 탐색
    if root.value < key:
        return search(root.right, key)
    # 그렇지 않으면 왼쪽으로 탐색
    else:    
        return search(root.left, key)
    
# 삭제
def minValueNode(node):
    # 왼쪽 자식 노드를 따라 최소값 노드를 찾아 반환
    current_node = node
    while current_node.left is not None:
        current_node = current_node.left
    return current_node


def delete(root, key):
    # 현재 노드가 없으면 반환
    if root is None:
        return root # root.left 또는 root.right에 None이 들어가면서 삭제가 구현됨

    # 삭제하려는 값이 현재 노드의 값보다 작으면 -> 왼쪽에서 삭제
    if key < root.value:
        root.left = delete(root.left, key) 
    
    # 삭제하려는 값이 현재 노드의 값보다 크면 -> 오른쪽에서 삭제
    elif key > root.value:
        root.right = delete(root.right, key)

    # 현재 노드의 값과 일치하는 경우 노드 삭제
    else:
        # 오른쪽 자식 먼저 올려주고 -> 없다면 왼쪽 자식
        # 현재 노드가 오른쪽 자식만 가지는 경우 또는 자식이 없는 경우
        if root.left is None:
            return root.right # 오른쪽 자식 or None을 현재 노드 자리로 올려준다. 
        
        # 현재 노드가 왼쪽 자식만 가지는 경우
        elif root.right is None:
            return root.left # 왼쪽 자식 or None을 현재 노드 자리로 올려준다. 
        
        # 현재 노드가 두 개의 자식 노드를 가지는 경우
        # 오른쪽 서브트리의 최소값 노드의 값을 현재 노드에 복사
        root.value = minValueNode(root.right).value
        # 복사된 값을 가지는 노드를 오른쪽 서브트리에서 삭제
        root.right = delete(root.right, root.value)

    return root
