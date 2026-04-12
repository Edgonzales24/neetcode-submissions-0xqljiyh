# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(node):
            if not node:
                return 0
            
            nonlocal res
            
            maxLeft = dfs(node.left)
            maxRight = dfs(node.right)
            maxLeft = max(maxLeft, 0)
            maxRight = max(maxRight, 0)

            res = max(res, node.val + maxLeft + maxRight)
            return node.val + max(maxLeft, maxRight)

        dfs(root)
        return res