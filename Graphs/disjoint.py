class disjontTree:
    parent = {}
    rank = {}
    size ={}
    def makeSet(self,arraydata):
        for i in arraydata:
            self.parent[i] = i 
            self.rank[i] = 0
            self.size[i] = -1

    def find(self,data):
        if self.parent[data] == data:
            return data
        else:
            return self.find(self.parent[data])
    
    def findpathcomp(self,data):
        if self.parent[data] == data:
            return data
        self.parent[data] = self.findpathcomp(self.parent[data]) 
        return self.parent[data]   
    
    def union(self,a,b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
            elif self.rank[x] > self.rank[y]:
                self.parent[y] = x
            else:
                self.parent[x] = y      
                self.rank[y] += 1
        else:
            return                
    def unionsize(self,a,b):
        x = self.find(a)
        y = self.find(b)
        if x!=y:
            if self.size[y]<self.size[x]:
                self.size[y] += self.size[x]
                self.parent[x] = y
            elif self.size[y]>self.size[x]:
                self.size[x] += self.size[y]
                self.parent[y] = x
            else:
                self.parent[x] = y
                self.size[y] += self.size[x]        
def printset(arrdata,ds):
    print([ds.find(i) for i in arrdata])
arraydata =[1,6,8,5,9]
ds = disjontTree()
ds.makeSet(arraydata)
printset(arraydata,ds)
ds.unionsize(8,5)
printset(arraydata,ds)
ds.unionsize(8,9)
printset(arraydata,ds)
# find(8)