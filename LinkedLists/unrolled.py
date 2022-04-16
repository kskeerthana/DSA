from array import array
from re import U


class Node():
    def __init__(self):
        self.length = 0
        self.array = []
        self.next = None

class UnrolledList():
    def __init__(self,capacity):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.nodeCount = 0
        # threshold = self.capacity / 2 + 1

    def insert(self,value):

        if(self.head == None):
            self.head = Node()
            self.nodeCount += 1
            self.head.array.append(value)
            self.head.length += 1
            self.tail = self.head

        elif(self.tail.length + 1 <= self.capacity):
            self.tail.array.append(value)
            self.tail.length += 1

        else:
            new_node = Node()
            self.nodeCount += 1
            half_length = self.tail.length// 2
            new_node.array.extend(self.tail.array[half_length:])

            new_node.array.append(value)
            self.tail.length = half_length
            new_node.length = len(new_node.array)

            self.tail.next = new_node
            self.tail = new_node            

    def traversal(self):
        temp = self.head
        while(temp):
            for i in range(temp.length):
                print(temp.array[i], end="\t")
            print()    
            temp = temp.next    
        print(self.nodeCount)

    def delete(self,value):
        temp = self.head
        # while(temp):
        #     for i in range (temp.length):
        #         if temp.array[i] == value:
        #             temp.array.pop(i)
        #             temp.array.append(None)
        #             temp.length -= 1        

                    # while temp.length < self.capacity // 2 and temp.next:
                    #     x = temp.next.array.pop(0)
                    #     temp.array.append(x)
                    #     temp.length +=1
                    #     temp.next.length -=1      

ull = UnrolledList(5)
ull.insert(2)
ull.insert(4)
ull.insert(6)
ull.insert(8)
ull.insert(10)
ull.insert(12)
# ull.insert(14)
# ull.insert(20)
# ull.insert(5)
# ull.insert(26)       
ull.traversal()
# ull.delete(6)
# ull.traversal()        