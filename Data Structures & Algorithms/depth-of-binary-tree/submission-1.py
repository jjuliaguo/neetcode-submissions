# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        #tree has already been built for u

        def dfs(node):
            #remember base case
            if not node:
                return 0 #have to start the number off

            leftH, rightH = dfs(node.left), dfs(node.right)
            # +1 to include root node
            return max(leftH, rightH)+1
        
        return dfs(root)

