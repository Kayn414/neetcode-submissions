# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = deque([root])

        while q:
            level_size = len(q)
            level_max = float('-inf')


            
            for i in range(level_size):
                node = q.popleft()
            
                level_max = max(level_max, node.val)
                    
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)

            res.append(level_max)


        res_ = [x for x in res if x != float('-inf')]

        return res_
            
                

            

                