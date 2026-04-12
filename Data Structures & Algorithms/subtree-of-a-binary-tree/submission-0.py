# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Base cases
        if not root:
            return False
        
        # Check if the tree starting at current node matches subRoot
        if self.isSameTree(root, subRoot):
            return True
        
        # If not, check left and right subtrees
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
    # If both are None, they're equal
        if not tree1 and not tree2:
            return True
        
        # If one is None and other isn't, they're not equal
        if not tree1 or not tree2:
            return False
        
        # Check current nodes and recursively check children
        return (tree1.val == tree2.val and 
                self.isSameTree(tree1.left, tree2.left) and 
                self.isSameTree(tree1.right, tree2.right))
            
        
        
        

        