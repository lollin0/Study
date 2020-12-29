# 노드 클래스 작성
class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

# 노드에 데이터를 추가할 함수 작성
def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)
    
# 노드 연결
nodeStart = Node("head시작")
head = nodeStart
# 노드에 1~9까지 데이터를 순서대로 넣음 
for data in range(1,10):
    add(data)
    
    
node = head # 연결된 노드들을 출력하기에 앞서 처음 시작한 head부분을 알아야 검색 가능
while node.next: # 노드에 포인터가 가리키는게 없을때까지 반복
    print(node.data)
    node = node.next
print(node.data)
