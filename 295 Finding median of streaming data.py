import bisect
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.sl = []

    def addNum(self, num: int) -> None:
        bisect.insort(self.sl,num)
        

    def findMedian(self) -> float:
        n = len(self.sl)
        
        if n == 1: 
            return self.sl[0]
        
        rem = n%2
        med = n//2
        
        if rem != 0:
            return self.sl[med]
        else:
            return float((self.sl[med] + self.sl[med-1]) /2)
        
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
