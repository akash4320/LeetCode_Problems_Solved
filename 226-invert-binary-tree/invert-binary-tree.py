# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postOrderTraversal(self,node):
        if node is None:
            return
        self.postOrderTraversal(node.left)
        self.postOrderTraversal(node.right)
        node.left,node.right = node.right, node.left

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root != None:
            self.postOrderTraversal(root)

        return root
        