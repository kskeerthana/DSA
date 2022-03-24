class TreeNode:
    def __init__(self,data=None):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

    # def height(self):
    #     return self.recursiveheight(root)

    # def recursiveheight(self,root):
    #     if root == None:
    #         return 
    #     else:
    #         leftHeight = self.recursiveheight(root.left)
    #         rightHeight = self.recursiveheight(root.right)

    #         if leftHeight>rightHeight:
    #             return 1+leftHeight
    #         else:
    #             return 1+ rightHeight     
    
    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    
    def getBalance(self,root):
        if root == None:
            return
        else:
            return self.getHeight(root.left) - self.getHeight(root.right)  
    
    def LeftRotate(self,z):
        temp = z.right 
        W = temp.left

        temp.left = z
        z.right = W  

        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        temp.height = 1 + max(self.getHeight(temp.left),self.getHeight(temp.right))
        return temp
    
    def RightRotate(self,y):
        temp = y.left
        X = temp.right
        
        temp.right = y
        y.left = X

        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        temp.height = 1 + max(self.getHeight(temp.left),self.getHeight(temp.right))

        return temp

    def Insert(self,root,value):
        if root == None:
            return TreeNode(value)
        elif value < root.data:
            root.left = self.Insert(root.left,value)
        else: 
            root.right = self.Insert(root.right,value)    

        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))

        balanceFactor = self.getBalance(root) 

        if balanceFactor > 1 and value < root.left.data :
            return self.RightRotate(root)

        if balanceFactor < -1 and value > root.right.data :
            return self.LeftRotate(root)

        if balanceFactor > 1 and value > root.left.data:
            root.left = self.LeftRotate(root.left)
            return self.RightRotate(root) 

        if balanceFactor < -1 and value < root.right.data:
            root.right = self.RightRotate(root.right)
            return self.LeftRotate(root.right)

        return root
    def delete(self,root,value):
        if root == None:
            return 
        if value < root.data:
            root.left = self.delete(root.left,value)
        elif value > root.data:
            root.right = self.delete(root.right,value)  
        else:
            if root.left == None:
                temp = root.right
                root = None
                return temp
            if root.right == None:
                temp = root.left
                root = None
                return temp  

            temp = self.FindMin(root.right)
            root.data = temp.data      
            root.right=self.delete(root.right,temp.data) 

        if root == None:
            return root
        
        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))

        balanceFactor = self.getBalance(root) 

        if balanceFactor > 1 and self.getBalance(root.left) >=0:
            return self.RightRotate(root)

        if balanceFactor < -1 and self.getBalance(root.right) <= 0:
            return self.RightRotate(root)

        if balanceFactor > 1 and self.getBalance(root.left) < 0 :
            root.left = self.LeftRotate(root.left)
            return self.RightRotate(root)

        if balanceFactor < -1 and self.getBalance(root.right) > 0 :
            root.right = self.RightRotate(root.right)
            return self.LeftRotate(root)  

        return root            

    def PreOrder(self,root):
        if root ==  None:
            return
        print(root.data,end='==>')   
        self.PreOrder(root.left)
        self.PreOrder(root.right)

    def FindMin(self,root):
        # current = root
        # if root == None:
        #     return
        # while current.left:
        #     current = current.left
        # return current      
        if root is None or root.left is None:
            return root
        return self.FindMin(root.left)

myTree = TreeNode()
root = None
 
root = myTree.Insert(root, 6)
root = myTree.Insert(root, 5)
root = myTree.Insert(root, 9)
root = myTree.Insert(root, 3)
root = myTree.Insert(root, 8)
root = myTree.Insert(root, 7)

print("Preorder traversal of the",
      "constructed AVL tree is")
myTree.PreOrder(root)
root = myTree.delete(root,8)
print('\n')
myTree.PreOrder(root)
# print("height:" , myTree.height())
print()