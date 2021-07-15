from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def canMerge(self, trees: List[TreeNode]) -> TreeNode:
        def isvalid(node, lower=float('-inf'), upper=float('inf')) -> bool:
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not isvalid(node.right, val, upper):
                return False
            if not isvalid(node.left, lower, val):
                return False
            return True

        if len(trees) == 1: return trees[0] if isvalid(trees[0]) else None
        tre_di = {}
        co_di, yy_di = {}, {}
        for i in trees:
            tre_di[i.val] = i
        for i in range(len(trees)):
            temp = trees[i]
            lc, rc = temp, temp
            while lc.left: lc = lc.left
            while rc.right: rc = rc.right
            t = [lc.val, rc.val]
            if lc == temp or lc.val not in tre_di: t.remove(lc.val)
            if rc == temp or rc.val not in tre_di: t.remove(rc.val)
            co_di[temp.val] = t
            for x in t:
                if x in yy_di:
                    yy_di[x].append(temp.val)
                else:
                    yy_di[x] = [temp.val]

        def jianshu(t, ta, tb, v):
            t.val = ta.val
            if ta.left and ta.left.val == v:
                t.left = tb
            elif ta.left:
                tl = TreeNode()
                t.left = tl
                jianshu(tl, ta.left, tb, v)
            if ta.right and ta.right.val == v:
                t.right = tb
            elif ta.right:
                tr = TreeNode()
                t.right = tr
                jianshu(tr, ta.right, tb, v)
            return t

        print(co_di)
        print(yy_di)
        for i in trees:
            iv = i.val
            a, b = len(co_di[iv]) if iv in co_di else 0, len(yy_di[iv]) if iv in yy_di else 0
            if a + b == 0: return None
            tempar = co_di[iv]
            for t in tempar:
                temp_tree = TreeNode()
                temp_tree = jianshu(temp_tree, i, tre_di[t], t) if t in tre_di else None
                if not isvalid(temp_tree):
                    co_di[iv].remove(t)
                    yy_di[t].remove(iv)
        root = None
        for i in trees:
            iv = i.val
            a, b = len(co_di[iv]) if iv in co_di else 0, len(yy_di[iv]) if iv in yy_di else 0
            if a + b == 0: return None
            if b == 0: root = i
        sss = set()

        def j(r):
            nonlocal sss
            sss.add(r.val)
            if not r: return None
            if r.left and r.left.val in co_di[r.val]:
                r.left = j(tre_di[r.left.val])
            if r.right and r.right.val in co_di[r.val]:
                r.right = j(tre_di[r.right.val])
            return r

        ans = j(root)
        print(sss)
        for i in tre_di:
            if i not in sss: return None

        return ans if isvalid(ans) else None

