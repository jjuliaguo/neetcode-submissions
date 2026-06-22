# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = 0

        #you have to know that the return of dfs is not the diameter but the height
        #essentially it gets the max heights and then calculates the diameter
        #so every recursive step, it adds 1 to the height on the sides 
        #then uses that to get the diameter
        
        def dfs(root):
            nonlocal maxDiam #use when u need to modify it

            if not root:
                return 0

            leftH = dfs(root.left) 
            rightH = dfs(root.right)
            #returns max height for u
            maxDiam = max(maxDiam, leftH + rightH)
            return max(leftH, rightH) + 1
        
        dfs(root)
        return maxDiam
        

        
