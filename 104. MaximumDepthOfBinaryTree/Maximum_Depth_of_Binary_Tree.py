# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Recursiv DFS :
        
        # Base Case , When Reach to Leaf node or Null Node
        if not root :
            return 0
        
        # Recursive call of both side,
        # Find max b/w them..
        # Add 1 for Root's Depth
        return 1 + max(self.maxDepth(root.left) , self.maxDepth(root.right))
