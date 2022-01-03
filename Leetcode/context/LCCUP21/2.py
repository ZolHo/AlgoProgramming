# @time   :2021/09/11
# @author :ZolHo
# @file   :2.py

from typing import List
from collections import deque
class Solution:
    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        ouq = deque()
        jiq = deque()
        ous = [i for i in cards if i%2==0]
        jis = [i for i in cards if i%2==1]
        ous.sort(reverse=True)
        jis.sort(reverse=True)
        ou, ji = len(ous), len(jis)
        if (cnt % 2 == 1):
            if ou < cnt and ou % 2 == 0: return 0
        i, j = 0, 0
        while cnt>0 :
            break


