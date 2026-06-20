# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return [True, 0]

            leftH, rightH = dfs(node.left), dfs(node.right)
            balanced = leftH[0] and rightH[0] and abs(leftH[1] - rightH[1]) <= 1
            return [balanced, max(leftH[1], rightH[1])+1]
        return dfs(root)[0]