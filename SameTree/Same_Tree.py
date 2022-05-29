# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both Are Empty Tree...
        if not q and not p :
            return True
        
        # If One of them is Empty or If Values are Diff...
        if not q or not p or p.val != q.val :
            return False
        
        # Recursive Call On Left And Right Child Of both
        return self.isSameTree(p.left , q.left) and self.isSameTree(p.right , q.right)
