# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        
        def dfs(root):
            if not root.left and not root.right:
                self.val = max(self.val, root.val)
                return root.val, root.val, root.val, True
            elif not root.left:
                mn2, mx2, t2, good = dfs(root.right)
                if good and mn2 > root.val:
                    self.val = max(self.val, t2 + root.val)
                    return root.val, mx2, t2 + root.val, True
            elif not root.right:
                mn1, mx1, t1, good = dfs(root.left)
                if good and mx1 < root.val:
                    self.val = max(self.val, t1 + root.val)
                    return mn1, root.val, t1 + root.val, True
            else:
                mn1, mx1, t1, good1 = dfs(root.left)
                mn2, mx2, t2, good2 = dfs(root.right)
                if good1 and good2 and mx1 < root.val < mn2:
                    self.val = max(self.val, t1 + t2 + root.val)
                    return mn1, mx2, t1 + t2 + root.val, True
            return -1, -1, -1, False
        
        self.val = 0
        dfs(root)
        return self.val
        
