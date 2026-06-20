# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Edge case: if there are no linked lists, return nothing
        if not lists or len(lists) == 0:
            return None

        # Keep merging until only ONE linked list remains
        while len(lists) > 1:

            # This will store the merged lists for the next round
            mergedLists = []

            # Go through the lists TWO at a time
            # i = 0, 2, 4, 6...
            for i in range(0, len(lists), 2):

                # First list in the pair
                l1 = lists[i]

                # Second list in the pair
                # If there isn't one (odd number of lists),
                # just use None
                if (i + 1) < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None

                # Merge the two sorted linked lists
                mergedLists.append(self.mergeList(l1, l2))

            # Replace the old list of lists with the newly merged ones
            lists = mergedLists

        # When only one list remains, that's our answer
        return lists[0]



    # Merge TWO sorted linked lists into ONE sorted linked list
    def mergeList(self, l1, l2):
        
        # Dummy node makes building the answer easier
        dummy = ListNode()

        # tail always points to the LAST node in our merged list
        tail = dummy

        # Continue while BOTH lists still have nodes
        while l1 and l2:

            # Choose the smaller value
            if l1.val < l2.val:

                # Add l1's node to the merged list
                tail.next = l1

                # Move l1 forward
                l1 = l1.next

            else:

                # Add l2's node instead
                tail.next = l2

                # Move l2 forward
                l2 = l2.next

            # Move tail forward because we added a node
            tail = tail.next

        # One list might still have leftover nodes.
        # Since it's already sorted, attach the rest directly.

        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        # dummy points before the real head,
        # so return the node after it
        return dummy.next