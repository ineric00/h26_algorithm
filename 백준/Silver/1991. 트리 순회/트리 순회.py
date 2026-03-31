import sys

num_node = int(sys.stdin.readline()) # 입력을 빠르게 받기 위해 sys 사용 권장

# 트리 생성하기
tree = {} 
for _ in range(num_node):
    # 공백 제거 후 분리
    root, left, right = sys.stdin.readline().split() 
    tree[root] = [left, right]

# 1. 전위 순회
def preorder(node):
    if node == '.':
        return
    print(node, end='')      # 본인 출력 (문제 조건상 공백 없이 붙여서 출력)
    preorder(tree[node][0])  # 왼쪽 자식 탐색
    preorder(tree[node][1])  # 오른쪽 자식 탐색

# 2. 중위 순회
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])
    print(node, end='')      # 본인 출력
    inorder(tree[node][1])

# 3. 후위 순회
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end='')      # 본인 출력

# 함수 호출 (print() 안에 넣지 않고 바로 호출)
preorder('A')
print()
inorder('A')
print()
postorder('A')