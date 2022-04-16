from tkinter.messagebox import NO


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DLinkedList:
    def __init__(self):
        self.head = None
        #self.count = None

    def get_count(self):
        head = self.head
        count = 0
        while(head):
            count += 1
            head = head.next
        return count

    def traversal(self):
        if self.head is None:
            print('Empty!')
        else:
            head = self.head
            while(head):
                print(head.data)
                head = head.next

    def insert_beginning(self,new_node):
        new_node = Node(new_node)
        if self.head is None:
            self.head = self.next = new_node
        else:
            new_node.prev = None
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.traversal()	
    
    def insert_end(self,new_node):
        new_node = Node(new_node)
        head = self.head
        while (head.next):
            head = head.next
        head.next = new_node
        self.traversal()
    
    def insert_at_pos(self,pos,new_node):
        new_node = Node(new_node)
        self.length = self.get_count()
        print('printing count value',self.length)
        if pos > self.length or pos < 0:
            return None
        else:
            if pos == 0 :
                self.insert_beginning(new_node)
                print('inserted at beg')
            else: 
                if pos == self.length:
                    self.insert_end(new_node)
                    print('inserted at end')
                else:
                    print('gonna inserted at pos')
                    current = self.head
                    count = 1
                    while count < pos-1 :
                        count += 1
                        current = current.next
                    new_node.next = current.next
                    current.next = new_node
                    self.length += 1			
        self.traversal()	

    def del_node(self,value):
        length = self.get_count()
        head = self.head
        if length == 0:
            print('list is empty')
        else:
            if(head is not None):
                if(head.data == value):
                    self.head = self.head.next
                    length -= 1
            while(head is not None):
                if (head.data == value):
                    break
                temp = head
                head = temp.next
            temp.next = head.next
            head = None	
            # else:
            # 	if  	
        self.traversal()		



linklist = DLinkedList()
linklist.head = Node(6)
link2 = Node(12)
link3 = Node(18)
link4 = Node(24)
link5 = Node(30)
linklist.head.next = link2
link2.next = link3
link3.next = link4
link4.next = link5

# linklist.traversal()
# linklist.insert_end()
linklist.insert_beginning(3)
# linklist.insert_at_pos(3,14)
# linklist.del_node(30)