# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = head
        while curr is not None:
            if curr.val == prev.val and curr != head:
                curr = curr.next
                prev.next = curr
            else:
                if prev != head:
                    prev = prev.next
                else:
                    prev = curr
                curr = curr.next
        return head
