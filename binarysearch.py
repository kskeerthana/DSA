class Node:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None

def insert(root,data):
    temp = root
    prev = None
    if root ==  None:
        root == Node(data)
        return root
    while(temp):
        prev = temp
        if temp.data>data:
            temp = temp.left
        else:
            temp = temp.right
    if prev.data > data:
        prev.left = Node(data)
    else:
        prev.right = Node(data)

def InOrder(root):
    if root ==  None:
        return
    InOrder(root.left)    
    print(root.data,end='==>')   
    InOrder(root.right)
def Search(root,value):
    current = root
    if root == None:
        return
    while(current):
        if current.data == value:
            return current.data    
        elif current.data > value:
            current = current.left
        else:
            current = current.right
    return current.data            

def FindMin(root):
    current = root
    if root == None:
        return
    while current.left:
        current = current.left
    return current      

def Delete(root,value):
    if root == None:
        return
    if value < root.data:
        root.left = Delete(root.left,value)
    elif value > root.data:
        root.right = Delete(root.right,value)

    else:
        if root.left == None and root.right == None:
            return None
        if root.left == None:
            temp = root.right
            root = None
            return temp
        if root.right == None:
            temp = root.left
            root = None
            return temp  

        temp = FindMin(root,root.right)
        root.data = temp.data      
        root.right=Delete(root.right,temp.data)
    # print(root.data)
    return root
# def constructBST(keys):
#     root = None
#     for key in keys:
#         root = insert(root, key)
#     return root

root = Node(9)
insert(root,4)
insert(root,8)
insert(root,10)
insert(root,15)
insert(root,2)
insert(root,6)
# print(InOrder(root))
# print(FindMin(root))
# print(Search(root,8))
print(Delete(root,8))
print(InOrder(root))              

