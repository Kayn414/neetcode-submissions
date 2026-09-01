"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #input [[2],[1,3],[2]]
        if not node:
            return None
        # create q 
        q = deque([node])
        oldGraph = {}
        oldGraph[node] = Node(node.val) # clone current node (1)

        while q:
            cur = q.popleft() # 1 
            
            for nb in cur.neighbors: # 2 
                if nb not in oldGraph: 
                    oldGraph[nb] = Node(nb.val) # create node 2 
                    q.append(nb) # 1, 2
                # Connect the cloned neighbor to the cloned current node (so connect node 1 and 2)
                oldGraph[cur].neighbors.append(oldGraph[nb])
        
        return oldGraph[node]