class Node():
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next
class Stack():
    def __init__(self,data=None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    def push(self,value):
        temp = Node()
        temp.data = value
        temp.next = self.head
        self.head = temp
        self.peek()

    def pop(self):
        if self.head == None:
            raise IndexError

        temp = self.head.data
        self.head = self.head.next 
        return temp       

    def peek(self):
        if self.head == None:
            raise IndexError
        print(self.head.data)    
    # def display(self):
    #     if self.head == None:
    #         print('Stack empty')
    #     temp = self.head
    #     while(self.head):
    #         print(self.head.data,'->',end=" ")   
    #         temp = temp.next     

newlist = ['one','two','three','four']
stack = Stack(newlist)
print('popped:',stack.pop())
# stack.head = Node(8)
# stack.push(12)
# stack.push(16)        


