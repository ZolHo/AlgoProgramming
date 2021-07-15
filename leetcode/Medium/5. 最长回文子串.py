class Solution:
    def longestPalindrome(self, s: str) -> str:
        ns = []
        for i in range(len(s)):
            ns.append('@')
            ns.append(s[i])
        ns.append('@')

        s = "".join(ns)

        ans = 1
        big = 1
        l = len(s)
        for i in range(1, l):
            for j in range(1, l):
                if i + j >= l or i - j < 0:
                    break
                if ns[i - j] == ns[i + j]:
                    if j > big:
                        big = j
                        ans = i
                else:
                    break
        return s[ans - big:ans + big + 1].replace('@', '')