class DSU:
    def __init__(self, n):
        self.comps = n
        self.Parent = list(range(n+1))
        self.Size = [1] * (n + 1)


    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self,x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py: # cycle
            return False
        # self.comps -= 1 
        if self.Size[px] < self.Size[py]:
            px, py = py, px 
        self.Size[px] += self.Size[py]
        self.Parent[py] = px
        return True

    def components(self):
        return self.comps

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        stack = []
        n = len(edges)
        dsu = DSU(n)
        for u,v in edges:
            stack.append([u,v])
            if not dsu.union(u,v):
                return stack.pop()
        
