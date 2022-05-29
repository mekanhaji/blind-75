# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive DFS Sol:
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Base Case , When Reach to Leaf node or Null Node
        if not root :
            return 0
        
        # Recursive call of both side,
        # Find max b/w them..
        # Add 1 for Root's Depth
        return 1 + max(self.maxDepth(root.left) , self.maxDepth(root.right))
# ------------------------------------------------------------------------------------------------------- #
# ITERATIVE DFS Sol:
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [ [root , 1] ]
        #  ^        ^     ^
        # Stack   Node  Depth of that node
        
        # Resulten Depth 
        res = 0
        
        # Stop when Stack in Empty  | Not Node left To pop from satck 
        while stack :
            node , depth = stack.pop()
        # ^ currNode its Depth poped From Stack
            
            # If curr node isn't null
            if node :
                
                # make res max of curr res and curr depth
                res = max(res , depth)
                
                # add(append) child of Curr Node To Stack
                # with + 1 to depth
                stack.append([node.left , depth + 1])
                stack.append([node.right , depth + 1])
        
        return res
