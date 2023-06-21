# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next

        while fast and fast.next: ## To get the slow pointer in the middle
            slow = slow.next
            fast = fast.next.next
        
        ## reverse the secound half list
        cur = slow.next
        prev = None
        slow.next = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp

        ## join the two list    

        first = head
        second = prev

        while first and second:
            temp1  = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2