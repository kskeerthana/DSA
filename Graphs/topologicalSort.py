class Vertex:
    def __init__(self,node):
        self.id = node
        self.adjacent = {}
        self.visited = False
        self.inDegree = 0

    def addNeighbour(self,neighbour,weight=0):
        self.adjacent[neighbour] = weight
    
    def getConnections(self):
        return self.adjacent.keys()
    
    def getVertexID(self):
        return self.id

    def getIndegree(self):
        return self.inDegree
    
    def setIndegree(self,data):
        self.inDegree = data        

class Graph:
    def __init__(self):
        self.verticesdict = {}
        self.numvertices = 0

    def __iter__(self):
        return iter(self.verticesdict.values()) 

    def addVertex(self,node):
        self.numvertices += 1
        newVertex = Vertex(node)
        self.verticesdict[node] = newVertex
    
    def addEdge(self,source,dest,cost=0):
        if source not in self.verticesdict:
            self.addVertex(source)
        if dest not in self.verticesdict:
            self.addVertex(dest)

        self.verticesdict[source].addNeighbour(self.verticesdict[dest],cost)
        # self.verticesdict[dest].addNeighbour(self.verticesdict[source],cost)

    def topoSort(self):
        topoSortList = []
        topoQ = []
        nodes = self.verticesdict.keys()
        remainingIn=[]
        # inDegree = {0:node for node in g}
        # for node in g:
        #     for neighbour in g[node]:
        #         neighbour.setIndegree(neighbour.getIndegree() + 1)

        for vert in g:
            indegree = vert.getIndegree()
            if indegree == 0:
                topoQ.append(vert)
            else:
                remainingIn[vert] = indegree        

        while len(topoQ):
            value = topoQ.pop(0)
            topoSortList.append(value)

            for child in value.getConnections():
                child.setIndegree(child.getIndegree() - 1)
                if child.getIndegree() == 0:
                    topoQ.append(child)

        if len(topoSortList)!=len(nodes):
            raise Exception("graph has a cycle")
        while(len(topoSortList)):
            node = topoSortList.pop(0)
            print('printing sorted list',node.getVertexID())        

g = Graph()
g.addVertex(5)
g.addVertex(4)
g.addVertex(2)
g.addVertex(3)
g.addVertex(1)
g.addVertex(0)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.topoSort()                          
