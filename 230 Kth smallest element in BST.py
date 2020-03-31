# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        nums = []
        def inOrder(node):
            if node:
                inOrder(node.left)
                nums.append(node.val)
                inOrder(node.right)
        inOrder(root)
        return nums[k-1]
        
