class Queue:
    def __init__(self,limit = None):
        self.Q = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def enQueue(self,value):
        if self.size >= self.limit:
            print('queue overflow')
            return 
        self.Q.append(value)

        if self.front == None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
            
        
        self.size += 1
        print(self.rear,self.front)
        print('after enqueing',self.Q)

    def deQueue(self):
        if self.size <= 0:
            print('queue underflow')
            return
        self.Q.pop(0)
        self.size -= 1
        if self.size == 0:
            self.front = self.rear = None
        self.rear = self.size - 1
        print('printing rear',self.rear,self.front)
        print('after dequeue',self.Q)                

queue = Queue(5)
queue.enQueue(5)
queue.enQueue(7)
queue.enQueue(8)
queue.enQueue(10)
queue.enQueue(12)
queue.deQueue()