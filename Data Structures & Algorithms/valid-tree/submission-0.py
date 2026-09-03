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
        self.comps -= 1 
        if self.Size[px] < self.Size[py]:
            px, py = py, px 
        self.Size[px] += self.Size[py]
        self.Parent[py] = px
        return True

    def components(self):
        return self.comps


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) >= n:
            return False
        
        dsu = DSU(n)
        for u, v in edges:
            if not dsu.union(u, v): 
                return False
        return dsu.components() == 1
