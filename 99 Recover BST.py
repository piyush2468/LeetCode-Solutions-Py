# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
                
        wrongVals=[]
        dfs(root,TreeNode(float("-inf")),wrongVals)
        #swap the values in the 2 wrong nodes
        wrongVals[0].val,wrongVals[1].val=wrongVals[1].val,wrongVals[0].val
        


def dfs(root,lastVisited,wrongVals):
    
    if root.left:
        lastVisited=dfs(root.left,lastVisited,wrongVals)
    
    if lastVisited.val>root.val: #found an out of order pair -> save them
        if wrongVals:
            wrongVals[1]=root
        else:#assume in the beginning that those are only the values that need to be swapped
            wrongVals+=[lastVisited,root]
    
    lastVisited=root
    
    if root.right:
        lastVisited=dfs(root.right,lastVisited,wrongVals)

    return lastVisited
