# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        result = []
        def zhongxu(node):
            if node == None:
                return
            if node.left:
                zhongxu(node.left)
            result.append(node.val)
            if node.right:
                zhongxu(node.right)
                zhongxu(root)
        ans = result[1] - result[0]
        for i in range (1, len(result)):
            if result[i] - result[i-1] < ans:
                ans = result[i] - result[i-1]
        return ans
