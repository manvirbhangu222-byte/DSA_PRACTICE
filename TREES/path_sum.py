class TreeNode(object):
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
class Solution():
    def isSamePath (self,root,targetSum):
        if root is None:
            return False
        if root.left is None and root.right is None:
            return targetSum==root.val
        
        left=self.isSamePath(root.left,targetSum-root.val)
        right=self.isSamePath(root.right,targetSum-root.val)
        return left or right 