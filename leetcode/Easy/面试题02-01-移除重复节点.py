# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if (head==None) :return head
        st, node = set([]), head
        st.add(head.val)
        while(node!=None and node.next!= None):
            while(node.next!= None and node.next.val in st) : node.next = node.next.next
            if(node == None or node.next==None) :break
            st.add(node.next.val)
            node = node.next
        return head
