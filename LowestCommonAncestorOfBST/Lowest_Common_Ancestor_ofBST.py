# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # if both p and q are less then root then...
        if p.val < root.val and q.val < root.val :
            
            # LCA will be in left side of tree.. 
            return self.lowestCommonAncestor(root.left , p , q)
        
        # if both p and q are greater then root then...
        if p.val > root.val and q.val > root.val :
            
            # LCA will be in right side of tree.. 
            return self.lowestCommonAncestor(root.right , p , q)
        
        # If p and q are Separated.. then comman perent node will be LCA
        return root
