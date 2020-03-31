class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        s = []
        s.append(head)
        res = db = Node(0, None, None, None)
        
        while s:
            node = s.pop()
            
            res.next = Node(node.val, res, None, None)
            res = res.next
            
            if node.next:
                s.append(node.next)
            
            if node.child:
                s.append(node.child)
        
        db.next.prev = None
        return db.next
