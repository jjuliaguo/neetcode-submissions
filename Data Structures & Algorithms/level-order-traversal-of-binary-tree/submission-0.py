# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def bfs(root):
            queue = deque()

            if root: #check if not empty
                queue.append(root)

            while len(queue) > 0:
                internalResult = []

                for i in range(len(queue)):
                    curr = queue.popleft()

                    internalResult.append(curr.val)

                    if curr.left: #if it exists
                    # if curr.left: -> not checking left right
                       
                        queue.append(curr.left)
                    # elif curr.right:
                    if curr.right:
                        queue.append(curr.right)
                #
                result.append(internalResult)

        bfs(root) #somehow iterate over everything and append the internal Results to the result
        return result

        