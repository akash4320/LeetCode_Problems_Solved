# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestNode(self,root):
        if root is None:
            return 0
        else:
            count = 0
            custQueue = []
            node = root
            custQueue.append(node)

            while not(len(custQueue) == 0):
                node = custQueue.pop(0)
                count += 1
                if node.left is not None:
                    custQueue.append(node.left)
                if node.right is not None:
                    custQueue.append(node.right)
            
            return math.floor(math.log(count,2))+1  

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        else:
            custQueue = []
            node_check = root
            custQueue.append(node_check)
            isBalanced = True

            while not(len(custQueue) == 0):
                node_check = custQueue.pop(0)
                isBalanced = abs(self.deepestNode(node_check.left) - self.deepestNode(node_check.right)) <= 1
                if not(isBalanced):
                    break;

                if node_check.left is not None:
                    custQueue.append(node_check.left)
                if node_check.right is not None:
                    custQueue.append(node_check.right)

            return isBalanced;
        