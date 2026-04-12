# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        arr = []

        def dfs(node):
            if not node:
                return None
            
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        return arr[k-1]

        # if not root: 
        #     return None

        # q = deque([root])
        # res = []

        # while q:
        #     for _ in range(len(q)):
        #         node = q.popleft()
        #         res.append(node.val)

        #         if node.left:
        #             q.append(node.left)
                
        #         if node.right:
        #             q.append(node.right)
            
        # res.sort()
        # print(res)
        # return res[k - 1]

        