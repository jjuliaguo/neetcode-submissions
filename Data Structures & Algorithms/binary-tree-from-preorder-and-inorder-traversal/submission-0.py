# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    #when ur job is to create a tree, don't use nested dfs()
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder or not inorder:
            return None

        #since preorder has its root first
        root = TreeNode(preorder[0])
        #don't need a hashmap
        #u just need where is the root inside inorder array
        mid = inorder.index(preorder[0])
        #in nested dfs(), you don't need self. since dfs() is a local function
        #here u do bcuz the method itself is the recursive function
        #whereas dfs() was local helper, recursive function

        #these different ranges help split into left and right
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid])
        
        root.right = self.buildTree(preorder[mid + 1 :], inorder[mid + 1 :])
        return root