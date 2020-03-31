class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        amap = {}
        for i in nums:
            if i in amap:
                amap[i] += 1
            else:
                amap[i] = 1
        for i in nums:
            for j in amap.keys():
                if -i - j in amap:
                    if i == j and j == -i-j:
                        if amap[i] > 2:
                            res.append(tuple(sorted([i, j, -i-j])))
                    elif i == j or i == -i-j:
                        if amap[i] > 1:
                            res.append(tuple(sorted([i, j, -i-j]))) 
                        if amap[i] > 1:
                            res.append(tuple(sorted([i, j, -i-j])))
                    elif j == -i-j:
                        if amap[j] > 1:
                            res.append(tuple(sorted([i, j, -i-j])))
                    else:
                        res.append(tuple(sorted([i, j, -i-j]))) 
        return list(set(res))
        
