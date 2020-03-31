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
           order=[]
		def inorder(root):
			if not root:return
			inorder(root.left)
			order.append(root)
			inorder(root.right)

		inorder(root)
		new=sorted(order,key=lambda x:x.val)
		for idx in range(len(order)):
			p,q=order[idx],new[idx]
			if p!=q:
				p.val,q.val=q.val,p.val
				break     
        



        



    


    





    

    




