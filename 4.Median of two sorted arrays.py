class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        num3 = num1 + num2
        num3.sort()
        if (len(num3) % 2 != 0):
            median = float(num3[int(len(num3)/2)])
            return median
        else:
            d = int(len(num3)/2) - 1
            median = (num3[d] + (num3[d+1])) / 2
            return median
        
        
