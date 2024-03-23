from collections import deque
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    def is_cyclic_connected(self, s):
        visited = [False] * self.V
        parent = [-1] * self.V
        q = deque()
        visited[s] = True
        q.append(s)
        while q:
            u = q.pop()
            for v in self.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
                    parent[v] = u
                elif parent[u] != v:
                    return True
        return False

    def is_cyclic_disconnected(self):
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i] and self.is_cyclic_connected(i):
                return True
        return False


# Driver Code
if __name__ == "__main__":
    V = 4
    g = Graph(V)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    if g.is_cyclic_disconnected():
        print("Yes")
    else:
        print("No")
