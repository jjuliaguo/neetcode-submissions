# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDiam = 0

        def dfs(root):
            nonlocal maxDiam

            if not root:
                return 0

            leftH = dfs(root.left) 
            rightH = dfs(root.right)
            #returns max height for u
            maxDiam = max(maxDiam, leftH + rightH)
            return max(leftH, rightH) + 1
        
        dfs(root)
        return maxDiam
        

        
