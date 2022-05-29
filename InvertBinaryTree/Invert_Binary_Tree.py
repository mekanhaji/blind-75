# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base Case 
        # when root become leaf node recursion will stop
        if not root :
            return None
        
        # Swap the left and right children..
        root.left , root.right = root.right , root.left
        
        # Recursion call on left child
        self.invertTree(root.left)
        
        # Recursion call on right child
        self.invertTree(root.right)
        
        return root
