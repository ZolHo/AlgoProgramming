class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        left, right = head, head
        if head.next == None:
            return None
        for i in range(n):
            right = right.next
        if right == None:
            return head.next
        while right.next != None:
            right = right.next
            left = left.next
        left.next = left.next.next
        return head
