# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        if not head or not head.next:
            return False

        fast = head
        slow = head

        while fast.next and fast.next.next and slow.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True

        return False
