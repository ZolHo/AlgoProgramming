from typing import List
from collections import Counter
class Solution:
    def sumGame(self, num: str) -> bool:
        ls , rs = num[:len(num)//2], num[len(num)//2:]
        lc, rc = Counter(ls), Counter(rs)
        suml, sumr, wenl, wenr = 0, 0, lc["?"], rc["?"]
        for i in range(1,10):
            suml += lc[str(i)]*i
            sumr += rc[str(i)] *i
        yu = wenl%2
        lmin, lmax = suml+ 9*(wenl//2+ yu), suml + 9*(wenl//2)
        if wenr %2 ==0 : rmin, rmax = sumr + 9*(wenr//2) , sumr+9*(wenr//2)
        elif yu ==0 : rmin, rmax = sumr + 9*(wenr//2 +1), sumr + 9*(wenr//2)
        else : rmin, rmax = sumr + 9*(wenr//2), sumr+9*(wenr//2+1)
        return True if rmax < lmin or rmin > lmax else False