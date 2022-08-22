# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        if not head:
            return head

        ans = head
        length = 0

        while head:
            length += 1
            head = head.next
        if n == length:
            return ans.next

        n = length - n - 1
        head = ans

        while n:
            head = head.next
            n -= 1
        head.next = head.next.next

        return ans
