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
            #note: leftH refers to the entire list itself
            balanced = leftH[0] and rightH[0] and abs(leftH[1] - rightH[1]) <= 1
            return [balanced, max(leftH[1], rightH[1])+1] #don't forget the [1] to access the number
        return dfs(root)[0] #returns the index 0 in dfs' returned