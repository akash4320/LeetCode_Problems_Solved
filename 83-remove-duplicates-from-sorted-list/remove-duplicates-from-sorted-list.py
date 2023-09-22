# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            prevNode = head
            currNode = head.next

            while currNode:
                if prevNode.val == currNode.val:
                    prevNode.next = currNode.next
                    currNode = currNode.next
                else:
                    prevNode = currNode
                    prevNode.val = currNode.val
                    currNode = currNode.next

        return head