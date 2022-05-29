# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# ------------------------------------------------------------------------------------------------------- #
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

# ------------------------------------------------------------------------------------------------------- #
# BFS Sol:
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # Base Case , When Reach to Leaf node or Null Node
        if not root :
            return 0
        
        depth = 0               # Depth counter
        queue = deque([root])   # Queue
        
        # Stop when Queue in Empty  | Not Node left To pop from Queue 
        while queue :
            
            # Go though all node in Queue
            for _ in range(len(queue)) :
                
                # Pop each Node
                node = queue.popleft()
                
                # Check If They Have Child
                # If So Then Add Or Append In Queue
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
            
            # Increase Depth Counter..
            depth += 1
        
        return depth
