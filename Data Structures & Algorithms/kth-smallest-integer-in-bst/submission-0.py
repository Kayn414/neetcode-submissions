# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = None

        def findMin(node):
            if not node:
                return 0

            findMin(node.left)
            self.count += 1
            if self.count == k:
                self.res = node.val
                return
            findMin(node.right)

            
        findMin(root)
        return self.res
