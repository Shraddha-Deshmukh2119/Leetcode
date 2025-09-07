# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        fast=head
        slow=head

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

        prev =None
        while slow:
            nxt=slow.next
            slow.next=prev
            prev=slow
            slow=nxt

        l,r=head,prev
        while r:
            if l.val!=r.val:
                return False
            l=l.next
            r=r.next
        return True            