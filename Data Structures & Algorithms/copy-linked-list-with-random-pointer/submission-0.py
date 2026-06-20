"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # Dictionary:
        # Original node -> Copied node
        #
        # defaultdict automatically creates a new Node(0)
        # whenever we access a node that isn't in the dictionary yet.
        oldToCopy = collections.defaultdict(lambda: Node(0))

        # If an original pointer is None,
        # the copied pointer should also be None.
        oldToCopy[None] = None

        # Start at the beginning of the original linked list
        cur = head

        # Visit every node in the original list
        while cur:

            # Copy the value from the original node
            oldToCopy[cur].val = cur.val

            # Connect the copied node's "next" pointer
            # to the copy of the original next node
            oldToCopy[cur].next = oldToCopy[cur.next]

            # Connect the copied node's "random" pointer
            # to the copy of the original random node
            oldToCopy[cur].random = oldToCopy[cur.random]

            # Move to the next original node
            cur = cur.next

        # Return the copied version of the original head
        return oldToCopy[head]