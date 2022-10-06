class Node():
    def __init__(self,data = None):
        self.data = data
        self.left = self.right = self.equal = None
        # self.isTerminating = False

class TST():
    def __init__(self,x = None):
        self.root = Node()
        self.leaf = x

    def _search(self,node,leaf):
        while node:
            if node.data == leaf:
                return node
            elif leaf< node.data:
                node = node.left
            else:
                node = node.right
        return None           

    def _insert(self,node,leaf):
        if node == None:
            return leaf
        elif leaf ==  node.data :
            return node
        elif leaf < node.data:
            node.left =  self._insert(node.left,leaf)
        else:
            node.right =  self._insert(node.right, leaf )
       
        return node             


    def Insert(self,string):
        cur_node = self.root
        for char in string:
            child = self._search(cur_node.equal,char)
            if not child:
                child = Node(char)
                cur_node.equal = self._insert(cur_node.equal,child)
            cur_node = child
        if not self._search(cur_node.equal,self.leaf):
            cur_node.equal = self._insert(cur_node.equal,Node(self.leaf))      


test_tst = TST()
test_tst.Insert('bella')
