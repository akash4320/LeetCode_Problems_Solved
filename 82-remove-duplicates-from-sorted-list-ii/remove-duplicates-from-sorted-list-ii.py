# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is not None:
            while head:
                if (head.next and head.val == head.next.val):
                    temp = head.val
                    head = head.next
                    while head and temp == head.val:
                        head = head.next
                else:
                    break;
        
        if head is not None and head.next is not None:
            currNode = head
            nextNode = currNode.next
            while nextNode and nextNode.next:
                if(nextNode.val == nextNode.next.val):
                    temp = nextNode.val
                    nextNode = nextNode.next
                    while nextNode and temp == nextNode.val:
                        nextNode = nextNode.next
                    
                    currNode.next = nextNode
                else:
                    currNode = currNode.next
                    nextNode = nextNode.next

        return head