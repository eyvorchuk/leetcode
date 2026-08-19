# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        seen = {}
        while curr is not None:
            if curr not in seen:
                seen[curr] = 0
            else:
                return curr
            curr = curr.next
        return None
