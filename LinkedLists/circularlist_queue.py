import re


class Node:
    def __init__(self,data = None):
        self.data = data 
        self.next = None

class CircularQueue:
    def __init__(self,data = None):
        self.rear = None
        self.front = None
        self.length = 0
        # if data:

    def enQueue(self,value):
        value = Node(value)
        if self.front == None:
            self.front = value
            # self.rear = value
        
        # while(self.rear.next != self.front):
        # #     self.rear.data = self.rear.next
        else:
            self.rear.next = value
        self.rear =  value
        self.rear.next = self.front    
            
        
        # print(self.rear.next)
        self.length += 1
        self.peek()        
        # value = Node()
        # value.data = value
        # value.next = self.head
        # current = self.head
        # if self.head == None:
        #     self.head = value
        # while(current.next != self.head):
        #     current = current.next
        # value.next = self.head
        # current.next = value
        # self.peek()
    def deQueue(self):
        temp =self.front
        #     # self.rear == None
        # else:
        #     self.front = temp.next
        # # if self.front == None:
        # #     self.rear = None    
        if self.front == None:
            print('Queue Empty')
        
        elif self.front == self.rear:
            self.rear=None
            self.front = None
            self.length = -1
            print(temp.data) 
        
        else:    
            # print(self.rear.data)
            self.front = self.front.next
            self.rear.next = self.front
            print(temp.data)    

    
    def peek(self):
        if self.front == None:
            raise IndexError
        print(self.rear.data,self.rear.next)
    # def display(self):
        


queue = CircularQueue()
queue.enQueue(4)
queue.enQueue(6)
# queue.enQueue(8)
# queue.enQueue(12)

queue.deQueue()
queue.deQueue()
queue.deQueue()
# queue.deQueue()
# newqueue = [2,4,6,8,10]