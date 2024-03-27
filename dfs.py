'''
from collections import defaultdict
class Graph:
	def __init__(self):
		self.graph = defaultdict(list)
	def addEdge(self, u, v):
		self.graph[u].append(v)

	def DFSUtil(self, v, visited):
		visited.add(v)
		print(v, end=' ')
		for neighbour in self.graph[v]:
			if neighbour not in visited:
				self.DFSUtil(neighbour, visited)
	def DFS(self, v):
		visited = set()
		self.DFSUtil(v, visited)

# Driver's code
if __name__ == "__main__":
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Following is Depth First Traversal (starting from vertex 2)")
	
	# Function call
	g.DFS(2)

# This code is contributed by Neelam Yadav
'''

from collections import defaultdict
class Graph:
    def __init__(self):
        self.adjlst=defaultdict(list)
    def addEdge(self,u,v):
        self.adjlst[u].append(v)
        
    def dfs(self,snode): 
              visited=set()
              self.dfsutil(snode,visited)
    def dfsutil(self,snode,visited):
        visited.add(snode)
        print(snode,end=" ")
        for neighbor in self.adjlst[snode]:
               if neighbor not in visited:
                      self.dfsutil(neighbor,visited)
                            
     
gg=Graph()
gg.addEdge(0,1)
gg.addEdge(0,2)
gg.addEdge(1,2)
gg.addEdge(2,0)
gg.addEdge(2,3)
gg.addEdge(3,3)

gg.dfs(2)
    

