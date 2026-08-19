# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        val = l1.val + l2.val
        if val >= 10:
            val = val - 10
            carry = 1
        else:
            carry = 0
        l3 = ListNode(val = val)
        l1 = l1.next
        l2 = l2.next
        prev = l3
        while l1 is not None and l2 is not None:
            val = l1.val + l2.val + carry
            if val >= 10:
                val = val - 10
                carry = 1
            else:
                carry = 0
            curr = ListNode(val = val)
            prev.next = curr
            prev = prev.next
            l1 = l1.next
            l2 = l2.next
        if l1 is None:
            while l2 is not None:
                val = l2.val + carry
                if val >= 10:
                    val = val - 10
                    carry = 1
                else:
                    carry = 0
                curr = ListNode(val = val)
                prev.next = curr
                prev = prev.next
                l2 = l2.next
        elif l2 is None:
            while l1 is not None:
                val = l1.val + carry
                if val >= 10:
                    val = val - 10
                    carry = 1
                else:
                    carry = 0
                curr = ListNode(val = val)
                prev.next = curr
                prev = prev.next
                l1 = l1.next
        if carry == 1:
            curr = ListNode(val = 1)
            prev.next = curr
        return l3

