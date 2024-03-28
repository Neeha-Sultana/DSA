'''
from collections import defaultdict as dd  

class Graph:  
    def __init__(self):  
        self.graph = dd(list)  

    def addEdgetoGraph(self, x, y):  
        self.graph[x].append(y)  
   

    def BFSearch(self, n):  
        visited_vertices = ( len(self.graph ))*[False]    
        queue = []  
        visited_vertices[n] = True  
        queue.append(n)  
        while queue:  
            n = queue.pop(0)  
            print (n, end = " ")     
            for v in self.graph[ n ]:  
                if visited_vertices[v] == False:  
                    queue.append(v)  
                    visited_vertices[v] = True  
  
# Example code  
# Initializing a graph  
graph = Graph()  
graph.addEdgetoGraph(0, 1)  
graph.addEdgetoGraph(1, 1)  
graph.addEdgetoGraph(2, 2)  
graph.addEdgetoGraph(3, 1)  
graph.addEdgetoGraph(4, 3)  
graph.addEdgetoGraph(5, 4)  
    
print ( " The Breadth First Search Traversal for The Graph is as Follows: " )  
graph.BFSearch(3)  
'''
from collections import defaultdict
class Graph:
    def __init__(self):
        self.adjlist=defaultdict(list)

    def addEdge(self,u,v):
        self.adjlist[u].append(v)

    def bfs(self,snode):
        visited=[False]*(len(self.adjlist))
        visited[snode]=True
        que=[]
        que.append(snode)
        while que:
            x=que.pop(0)
            print(x,end=" ")
            for i in self.adjlist[x]:
                if visited[i]==False:
                    visited[i]=True
                    que.append(i)


gg=Graph()
gg.addEdge(0,1)
gg.addEdge(1,1)
gg.addEdge(2,2)
gg.addEdge(3,1)
gg.addEdge(4,3)
gg.addEdge(5,4)
gg.bfs(3)
