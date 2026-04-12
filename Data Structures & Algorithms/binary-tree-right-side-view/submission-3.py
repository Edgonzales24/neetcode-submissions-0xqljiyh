# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque([root])

        while q:
            qLen = len(q)
            rightSide = None
            for i in range(qLen):
                root = q.popleft()
                if root:
                    rightSide = root
                    q.append(root.left)
                    q.append(root.right)
            if rightSide:
                res.append(rightSide.val)
        return res