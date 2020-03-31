class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        
        def traverse(root, d=dict()):
            if root == None: return 0, d
            lsum, _ = traverse(root.left, d=d)
            rsum, _ = traverse(root.right, d=d)
            sum_ = lsum+rsum+root.val
            d[sum_] = 1 if sum_ not in d else d[sum_]+1 
            return sum_, d
        
        _ ,d = traverse(root)
        if len(d) == 0: return []
        max_freq = max(d.values())
        ans = []
        for k,v in d.items():
            if v == max_freq:
                ans.append(k)
        return ans
