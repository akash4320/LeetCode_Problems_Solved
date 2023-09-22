# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
    
        while node != None:
            if node.val == 'check':
                return True
    
            node.val = 'check'
            node = node.next
            
        return False