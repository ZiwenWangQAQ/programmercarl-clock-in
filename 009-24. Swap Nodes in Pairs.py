# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head):
        if not head or not head.next:
            return head

        tmp = head.next
        head.next = tmp.next
        tmp.next = head
        ans = tmp
        while head.next and head.next.next:
            tmp = head.next
            head.next = head.next.next
            tmp.next = head.next.next
            head.next.next = tmp
            head = tmp

        return ans

