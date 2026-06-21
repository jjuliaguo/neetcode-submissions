# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        #less efficient, compare the arrays after sort

        #more efficient, compare as u traverse bst

        #probably use bfs to do level by level first

        queueQ = deque([p])
        queueP = deque([q])

        while len(queueQ) > 0 and len(queueP) > 0:
            for i in range(len(queueQ)):
                currQ = queueQ.popleft()
                currP = queueP.popleft()
                if not currQ and not currP:
                    continue
                if not currQ or not currP:
                    return False
                if currQ.val != currP.val:
                    return False
                #forgot to also check for right
                if (currQ.right is None) != (currP.right is None):
                    return False
                if currQ.left and currP.left:
                        queueQ.append(currQ.left)
                        queueP.append(currP.left)
                if currQ.right and currP.right:
                        queueQ.append(currQ.right)
                        queueP.append(currP.right)
                if (currQ.left is None) != (currP.left is None):
                    return False

        return True