# @time   :2021/07/18
# @author :ZolHo
# @file   :1.py

from typing import List
from collections import Counter

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        tset = [Counter(i).keys() for i in text.split(" ")]
        bset = Counter(brokenLetters).keys()
        ans = 0
        for i in tset :
            if len(i &bset) >0:
                continue
            else:
                ans += 1
        return ans