# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is not None: 
            total_elem = 0
            currNode = head

            while currNode:
                total_elem += 1
                currNode = currNode.next

            ind = 0
            currNode = head

            while ind < total_elem-n-1:
                ind += 1
                currNode = currNode.next

            if (currNode == head and currNode is None):
                head = None
            elif (currNode == head and currNode is not None and n == total_elem):
                head = head.next
            else:
                removeNode = currNode.next
                currNode.next = removeNode.next
        return head