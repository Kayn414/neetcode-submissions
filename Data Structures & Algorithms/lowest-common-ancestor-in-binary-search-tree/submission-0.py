# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parent = {root: None}
        que = deque([root])

        while que:
            node = que.popleft()

            if node.left:
                parent[node.left] = node
                que.append(node.left)
            if node.right:
                parent[node.right] = node
                que.append(node.right)


        ancestors = set()

        while p:
            ancestors.add(p)
            p = parent[p]
        
        while q not in ancestors:
            q = parent[q]

        return q 