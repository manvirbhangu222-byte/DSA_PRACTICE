class Treenode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left
        
class Solution(object):
    def maxDepth(self,root):
        if root is None:
            return None
        return 1 + max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        )
        