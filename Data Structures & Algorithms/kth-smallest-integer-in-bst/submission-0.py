# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root: 
            return None

        q = deque([root])
        res = []

        while q:
            for _ in range(len(q)):
                node = q.popleft()
                res.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            
        res.sort()
        print(res)
        return res[k - 1]

        