# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val):
        while head:
            if head.val == val:
                head = head.next
            else:
                break

        if not head:
            return head

        ans = head
        while head and head.next:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next

        return ans
