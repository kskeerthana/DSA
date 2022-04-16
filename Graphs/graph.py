class Vertex:
    def __init__(self,node):
        self.id = node
        self.adjacent = {}
        self.visited = False

    def addNeighbour(self,neighbour,weight=0):
        self.adjacent[neighbour] = weight
    
    def getConnections(self):
        return self.adjacent.keys()
    
    def getVertexID(self):
        return self.id

    def getWeight(self,neighbour):
        return self.adjacent[neighbour]    
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
        # directed graph
        self.verticesdict[source].addNeighbour(self.verticesdict[dest],cost)
        self.verticesdict[dest].addNeighbour(self.verticesdict[source],cost)

    def getEdges(self):
        edges = []
        for v in G:
            for w in v.getConnections():
                vid = v.getVertexID()
                wid = w.getVertexID()
                edges.append((vid,wid,v.getWeight(w)))
        return edges        

    def dfs(self,currVert,visited):
        visited[currVert] = True
        print("traversal: ",currVert.getVertexID())
        print(visited.values())
        for vertex in currVert.getConnections():
            if vertex not in visited:
                self.dfs(vertex,visited)        
                
    def DFSTraversal(self):
        visited = {}        
        for currVert in G:
            if currVert not in visited:
                self.dfs(currVert,visited)

    def BFSTraversal(self,currVert,visited):
        visited = {}
        BFSqueue = []
        visited[currVert] = True
        BFSqueue.append(currVert)
        while(BFSqueue):
            BFSqueue.pop(0)
            for vertices in currVert.getConnections():
                if vertices not in visited:
                    BFSqueue.append(vertices)
                    visited[vertices] = True

if __name__ == '__main__':
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addVertex('f')
    G.addEdge('a','b',4)
    G.addEdge('a','c',1)
    G.addEdge('c','b',2)
    G.addEdge('b','e',4)
    G.addEdge('c','d',4)
    G.addEdge('d','e',4)
    G.addEdge('e','f',1)
    G.DFSTraversal()
    print('Graph data:')
    print(G.getEdges())