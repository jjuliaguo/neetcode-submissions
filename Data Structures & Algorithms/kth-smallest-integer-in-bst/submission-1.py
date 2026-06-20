# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        #don't u just do dfs and get an array
        #make sure to append the Null ones too
        #then return the number at that index?

        result = []

        def dfs(node):
            #this checks if its a leaf
            #if not node.left and not node.right:
            if not node: #checks if this node exists
                #this check is redundant, if 
                # if node == None: #should be == not !=
                    return node
            
            dfs(node.left) #u can assume that the result.append handles the adding to list
            result.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return result[k-1]