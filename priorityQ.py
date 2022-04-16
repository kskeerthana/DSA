class PQ:
    def __init__(self):
        self.items = [0]

    def __len__(self):
        return len(self.items) - 1
    
    def minChild(self,i):
        if i * 2 + 1 > len(self):
            return i * 2
        else:
            if self.items[i*2] < self.items[i * 2 + 1]:
                return i * 2
            return i * 2 + 1                    
    
    def percolateUp(self):
        i = len(self)
        while i // 2 > 0:
            if self.items[i] < self.items[i//2]:
                self.items[i//2],self.items[i] = self.items[i],self.items[i//2]
            i = i//2
        print(self.items)    
    
    def percolate_down(self, i):
        while i * 2 <= len(self):
            mc = self.minChild(i)
            if self.items[i] > self.items[mc]:
                self.items[i], self.items[mc] = self.items[mc], self.items[i]
            i = mc

    def insert(self,data):
        self.items.append(data)
        self.percolateUp()       

    def delete(self):
        return_value = self.items[1]
        self.items[1] = self.items[len(self)]
        self.items.pop()
        self.percolate_down(1)
        print(self.items)
        return return_value
        
PriorityQ = PQ()
PriorityQ.insert(9)
PriorityQ.insert(5)
PriorityQ.insert(6)
PriorityQ.insert(2)
PriorityQ.insert(3)
PriorityQ.delete()