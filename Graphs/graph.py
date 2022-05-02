import heapq
import sys
from disjoint import disjontTree

class Vertex:
    def __init__(self,node):
        self.id = node
        self.adjacent = {}
        self.visited = False
        self.distance = sys.maxsize

    def addNeighbour(self,neighbour,weight=0):
        self.adjacent[neighbour] = weight
    
    def getConnections(self):
        return self.adjacent.keys()
    
    def getVertexID(self):
        return self.id

    def getWeight(self,neighbour):
        return self.adjacent[neighbour]   

    def setDistance(self,value):
        self.distance = value

    def getDistance(self):
        return self.distance    

    def setVisited(self):
        self.visited = True      

    def __lt__(self,nxt):
        return self.id < nxt.id

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
        # self.verticesdict[dest].addNeighbour(self.verticesdict[source],cost)

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
    def dijkstra(self,value):
        print('dijstra:',value.getVertexID())
        unvisited_nodes = list(self.verticesdict.values())
        shortest_path = {}
        previous_nodes = {}
        max_value = sys.maxsize
        
        #setting the distance for all vertices to max
        for node in unvisited_nodes:
            shortest_path[node] = max_value
        shortest_path[value] = 0

        #finding the min element
        while unvisited_nodes:
            min_node = None
            for node in unvisited_nodes:
                if min_node ==None:
                    min_node = node
                if shortest_path[node] < shortest_path[min_node]:
                    min_node = node
            #updating the weights in the shortest path and previous node dicts
            for node in min_node.getConnections():
                temp = shortest_path[min_node] + min_node.getWeight(node)   
                if temp <  shortest_path[node]:
                    shortest_path[node] = temp
                    previous_nodes[node] = min_node 

            unvisited_nodes.remove(min_node)
        print(shortest_path.values())
        return shortest_path,previous_nodes  

        
    def prims(self,source):
        source.setDistance(0)
        # k = source.getDistance()
        unvisited_queue = [(v.getDistance(),v) for v in G]
        # unvisited_queue=[]
        # for value in G:
        #     heapq.heappush(unvisited_queue,(value.getDistance(),value))
        # print(unvisited_queue)
        # print(type(unvisited_queue[0]))
        # sorted(unvisited_queue)
        heapq.heapify(unvisited_queue)
        while len(unvisited_queue):
            node = heapq.heappop(unvisited_queue)
            current = node[1]
            # print('current:',current)
            current.setVisited()
            for values in current.getConnections():
                if values.visited:
                    continue
                newCost = current.getWeight(values)
                if newCost < values.getDistance():
                    values.setDistance(newCost)
                    print('Updated: current:{},next:{},newcost:{}'.format(current.getVertexID(),values.getVertexID(),values.getDistance()))
                else:
                    print('Not Updated: current:{},next:{},newcost:{}'.format(current.getVertexID(),values.getVertexID(),values.getDistance()))

            # while len(unvisited_queue):
            #     heapq.heappop(unvisited_queue)
            # unvisited_queue = [(v.getDistance(),v) for v in G]
            # heapq.heapify(unvisited_queue)    
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
    def kruskal(self):
        edges =[]
        for v in G:
            self.makeSet(v.getVertexID())
            for w in v.getConnections():
                vid = v.getVertexID()
                wid = w.getVertexID()
                edges.append((v.getWeight(w),vid,wid))
        # print(edges) 
        edges.sort()        
        mst = set()
        for edge in edges:
            weight, vertice1, vertice2 = edge
            # print(weight,vertice1,vertice2)
            if self.find(vertice1) != self.find(vertice2):
                self.union(vertice1,vertice2)
                mst.add(edge)
        print(mst)        
        return mst    



if __name__ == '__main__':
    G = Graph()
    G.addVertex('a')
    G.addVertex('b')
    G.addVertex('c')
    G.addVertex('d')
    G.addVertex('e')
    G.addVertex('f')
    G.addVertex('g')
    G.addVertex('h')
    G.addVertex('i')
    G.addEdge('a','b',4)
    G.addEdge('a','c',8)
    G.addEdge('b','c',11)
    G.addEdge('b','d',8)
    G.addEdge('c','e',7)
    G.addEdge('c','f',1)
    G.addEdge('d','g',7)
    G.addEdge('d','h',4)
    G.addEdge('g','h',14)
    G.addEdge('g','i',9)
    G.addEdge('h','i',10)
    # G.addEdge('a','b',4)
    # G.addEdge('a','c',1)
    # G.addEdge('c','b',2)
    # G.addEdge('b','e',4)
    # G.addEdge('c','d',4)
    # G.addEdge('d','e',4)
    # G.addEdge('e','f',1)
    # G.DFSTraversal()
    # for value in G:
    #     G.dijkstra(value)
    # print(G.verticesdict.keys(),dir(G.verticesdict.values()))
    # for value in G:
    #     G.prims(value)
    G.kruskal()
    # print('Graph data:')
    # print(G.getEdges())
    # https://medium.com/survata-engineering-blog/monitoring-memory-usage-of-a-running-python-program-49f027e3d1ba