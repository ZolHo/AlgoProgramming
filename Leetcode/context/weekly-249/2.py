from typing import List
from collections import Counter
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        char_dict = {}
        for i, t in enumerate(s):
            if t in char_dict:
                char_dict[t].append(i)
            else :
                char_dict[t] = [i]
        ans = 0
        for i in "abcdefghijklmnopqrstuvwxyz" :
            if i in char_dict:
                ar0 = char_dict[i]
                if len(ar0) >= 2:
                    tempstr = s[ar0[0]+1:ar0[-1]]
                    c = Counter(tempstr)
                    ans += len(c)

        return ans

