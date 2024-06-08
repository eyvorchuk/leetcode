# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        def getLength(head):
            length = 0
            while head is not None:
                head = head.next
                length += 1
            return length
        
        currA = headA
        currB = headB
        lenA = getLength(currA)
        lenB = getLength(currB)
        currA = headA
        currB = headB
        if lenA > lenB:
            for i in range(lenA-lenB):
                currA = currA.next
        else:
            for i in range(lenB-lenA):
                currB = currB.next
        while currA != currB and currA is not None and currB is not None:
            currA = currA.next
            currB = currB.next
        if currA == currB:
            return currA
        else:
            return None
    
