# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root:
            return None
        
        #dont check for this?
        #implied in the base case
        #if root.left and root.right:

        #also if either left or right
        #we want to swap it (include null values)
        #so we don't need to factor them in
        
        #dont need a temp -> can just switch straight up
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root