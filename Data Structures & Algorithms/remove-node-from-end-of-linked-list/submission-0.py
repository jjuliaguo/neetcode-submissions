# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        headTracker = ListNode(0, head)
        #note: slow has to start 1 ahead to access previous node
        slow, fast = headTracker, head

        while n>0 and fast:
            fast = fast.next
            n -= 1

        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return headTracker.next
