# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        carryOver = 0

        while l1 or l2 or carryOver:
            if l1:
                first = l1.val
            else: 
                first = 0
            if l2:
                second = l2.val
            else:
                second = 0
            
            sum = first + second + carryOver
            carryOver = sum // 10
            sum = sum % 10
            curr.next = ListNode(sum)

            curr = curr.next
            if l1:
                l1 = l1.next
            else:
                l1 = None
            if l2:
                l2 = l2.next
            else:
                l2 = None
        
        return dummy.next