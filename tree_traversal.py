class Tree:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def PreOrder(root):
    if root ==  None:
        return
    print(root.data,end='==>')   
    PreOrder(root.left)
    PreOrder(root.right)

def PreOrderIter(root):
    if root == None:
        return
    stack =[]
    stack.append(root)
    while stack:
        node = stack.pop()
        print(node.data,end='==>')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)           

def InOrder(root):
    if root ==  None:
        return
    InOrder(root.left)    
    print(root.data,end='==>')   
    InOrder(root.right)
def InOrderIter(root):
    if root == None:
        return
    stack =[]
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack.pop()
            print(node.data, end= '==>')
            node = node.right    

def PostOrder(root):
    if root ==  None:
        return
    PostOrder(root.left)       
    PostOrder(root.right)
    print(root.data,end='==>')
def PostOrderIter(root):
    if root ==  None:
        return
    stack =[]
    node= root
    previous = None
    while stack or node:
        while(node):
            stack.append(node)
            node = node.left
        node =stack[-1]
        if not node.right or node.right == previous:
            previous = stack.pop()
            print(node.data,end='==>')
            node = None
        else:
            node = node.right    

class Queue:
    def __init__(self):
        self.queue = []
    def Enqueue(self,data):
        self.queue.append(data)
    def Dequeue(self):
        return self.queue.pop(0)
    def isEmpty(self):
        return len(self.queue)==0           
def LevelOrder(root):
    if root == None:
        return
    queue = Queue()
    queue.Enqueue(root)
    while not queue.isEmpty():
        temp =queue.Dequeue()
        print(temp.data,end='==>')
        if temp.left:
            queue.Enqueue(temp.left)
        if temp.right:
            queue.Enqueue(temp.right)    

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.left = Tree(6)
root.right.right = Tree(7)
# print(PreOrder(root))
# print(PreOrderIter(root))
# print(InOrder(root))
# print(InOrderIter(root))
# print(LevelOrder(root))
# print(PostOrder(root))
print(PostOrderIter(root))