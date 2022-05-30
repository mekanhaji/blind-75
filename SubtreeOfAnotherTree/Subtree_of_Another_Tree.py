# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If subRoot in null tree then it's also a sub tree of any tree..
        if not subRoot : return True
        
        # if root tree is null but subRoot is not...
        # then subRoot never be a subtree of root
        if not root : return False
        
        # if they are same trees then they are also subtree of each other..
        if self.sameTree(root , subRoot) : return True
        
        # Recursive Call On Left And Right Child Of both
        return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot)
    
    
    # Helper Function for checking if they are same tree
    def sameTree(self , p , q) :
        if not p and not q : return True
        if not p or not q or p.val != q.val : return False
        
        return (self.sameTree(p.left , q.left) and
                self.sameTree(p.right , q.right))

#--------------------------------------------------------------------------------------------------#
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
		#recursive function to check identity
        def isSame(r1, r2):
            if r1 == None and r2 == None:
                return True
            if r2 == None or r1 == None:
                return False
            else:
                if r1.val == r2.val: #if instance looks promising, check children
                    return isSame(r1.left, r2.left) and isSame(r1.right, r2.right)
            return False
        
		#use DFS to traverse
        q = deque([root])
        while q:
            cur = q.popleft()
            if isSame(cur, subRoot):
                return True
            else:
                if cur.right: q.append(cur.right)
                if cur.left : q.append(cur.left)
        
        return False
