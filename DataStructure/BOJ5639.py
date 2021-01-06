import sys
sys.setrecursionlimit(10**9)
'''
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        
class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        self.root = self._insert_value(self.root, data)
        return self.root is not None

    def _insert_value(self, node, data):
        if node is None:
            node = Node(data)
        else:
            if data <= node.data:
                node.left = self._insert_value(node.left, data)
            else:
                node.right = self._insert_value(node.right, data)
        return node
    
    def LRD(self):
        def _LRD(root):
            if root is None:
                pass
            else:
                _LRD(root.left)
                _LRD(root.right)
                print(root.data)
        _LRD(self.root)
        '''
def postorder(start, end):
    if start>end:
        return
    division = end + 1
    for i in range(start + 1, end + 1):
        if array[start] < array[i]:
            division = i
            break
    postorder(start+1, division -1)
    postorder(division, end)
    print(array[start])
    
array = []
limit = 0
while limit <= 10000:
    try:
        num = int(input())
    except: break
    array.append(num)
    limit+=1
postorder(0, len(array)-1)
