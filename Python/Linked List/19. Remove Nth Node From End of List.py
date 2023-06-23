# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        cur.next = head

        first = cur
        second = head

        while n and second:
            second = second.next
            n -= 1

        while second:
            first = first.next
            second = second.next
        
        first.next = first.next.next

        return cur.next