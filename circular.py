
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        #self.count = None

    def get_count(self):
        head = self.head
        if head == None:
            return 0 
        count = 1
        head = head.next
        while(head is not self.head):
            print(head.data)
            head = head.next
            count += 1
        print(count)  
        return count
    
    def traversal(self):
        head = self.head
        if head == None:
            return 0
        print(head.data)    
        head = head.next
        while(head is not self.head):
            print(head.data)
            head = head.next    
    
    def insert_at_end(self,new_node):
        new_node = Node(new_node)
        current = self.head

        if self.head == None:
            self.head = new_node
        else:
            while(current.next is not self.head):
                current = current.next
            new_node.next = self.head
            current.next = new_node
            self.traversal()         
    
    def insert_at_beg(self,new_node):
        new_node = Node(new_node)
        current = self.head
        
        if current == None:
            print('empty')
        
        new_node.next = current
        while (current.next is not self.head):
            current = current.next
        current.next = new_node    
        self.head = new_node
        self.traversal()

linklist = LinkedList()
linklist.head = Node(6)
link2 = Node(12)
link3 = Node(18)
link4 = Node(24)
link5 = Node(30)
linklist.head.next = link2
link2.next = link3
link3.next = link4
link4.next = link5
link5.next = linklist.head

# linklist.get_count()
# linklist.traversal()
# linklist.insert_at_beg(36)
linklist.insert_at_beg(3)