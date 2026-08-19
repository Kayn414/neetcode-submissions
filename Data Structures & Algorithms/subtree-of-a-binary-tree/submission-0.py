# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False 

        def isSameTree(p, q):
            if not p and not q:
                return True
            if not p or not q or p.val != q.val:
                return False
            return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node.val == subRoot.val and isSameTree(node, subRoot):
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return False 
