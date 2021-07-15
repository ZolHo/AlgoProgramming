from typing import List
from collections import Counter
class Solution:
    def minSwaps(self, s: str) -> int:
        c = Counter(s)
        if abs(c["0"]-c["1"]) >1 :
            return -1
        t = ""
        if c["0"] != c["1"] :
            if c["0"] > c["1"] :
                t = "0"
                for i in range(c["1"]):
                    t += "10"
            else:
                t = "1"
                for i in range(c["0"]) :
                    t += "01"
            dif = 0
            for i in range(len(s)):
                if t[i] != s[i] :
                    dif+=1
            return dif//2
        else:
            t1 = ["01" for i in range (c["0"])]
            t2 = ["10" for i in range (c["1"])]
            t1, t2 = "".join(t1), "".join(t2)

            dif1 , dif2 = 0, 0
            for i in range(len(s)):
                if t1[i] != s[i] :
                    dif1+=1
                if t2[i] != s[i] :
                    dif2+=1
            return min(dif1,dif2)//2

