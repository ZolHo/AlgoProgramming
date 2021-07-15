# 反转每对括号间的子串 1190
# 2021-05-26 22:26:45

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def reverseParentheses(self, s):
        if "(" not in s :
            return s
        lft, rit = -1, len(s)
        s = list(s)
        while lft < rit:
            while lft < rit:
                lft += 1
                if s[lft] in "()": break
            while lft < rit:
                rit -= 1
                if s[rit] in "()": break
            if lft > rit: break
            t = s[lft+1: rit]
            t.reverse()
            s[lft], s[rit] = "", ""
            for j in range(lft+1, rit) :
                s[j] = t[j-lft-1]
        return "".join(s)
# leetcode submit region end(Prohibit modification and deletion)
