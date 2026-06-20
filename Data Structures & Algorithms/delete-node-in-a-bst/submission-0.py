# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        #if a leaf
        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else: #when equals the value

            #this should be if it doesn't have a left child, return right
            #ur supposed to replace that node with the right child

            #if has left child
            if not root.left:
                return root.right
            #if has right child
            elif not root.right:
                return root.left
            else: 
                #check for the max
                currentNode = root.right
                while currentNode.left:
                    currentNode = currentNode.left
                root.val = currentNode.val
                root.right = self.deleteNode(root.right, root.val)

        return root

