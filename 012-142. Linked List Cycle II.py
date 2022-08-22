# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        if not head or not head.next:
            return None

        fast = head
        slow = head
        start = head

        while fast.next and fast.next.next and slow.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                while start != fast:
                    start = start.next
                    fast = fast.next
                return start

        return None
