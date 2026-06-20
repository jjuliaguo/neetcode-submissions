# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = [] #this is the order list it returns

        #base case must be in the recursive method
        #if not root:
            #return root

        #can keep the return type as understandable purposes
        #doesn't change what it does
        def inorder(opt: Optional[TreeNode]):
            if not opt: #check opt not rootwhat happens if it calls root
                return opt #not checking if og tree is empty
                #checking if the node i'm currently visiting is empty
        
            #the left and right recursive calls will append their own nodes
            #current function only appends its own nodes
            inorder(opt.left) 
            result.append(opt.val)
            inorder(opt.right)
        #actually have to call the inorder method that we created
        inorder(root)
        return result