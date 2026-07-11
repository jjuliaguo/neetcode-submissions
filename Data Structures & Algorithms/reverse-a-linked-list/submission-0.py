# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #you're given the head, not the linkedlist called head
        #bcuz of pointers, you get access to entire linkedlist that way
    
        prev = None
        #this declaration enables you to start the while loop
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev