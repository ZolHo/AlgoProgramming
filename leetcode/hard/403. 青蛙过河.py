from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        mydict = {}
        for i in stones:
            mydict[i] = set([])
        mydict[0].add(0)
        for v in stones:
            if len (mydict[v]) == 0 :
                continue
            for j in mydict[v]:
                for k in range(j-1,j+2):
                    if k<=0:
                        continue
                    if (k+v) in mydict:
                        mydict[k+v].add(k)
        # print(mydict)
        return len (mydict[stones[-1]] ) > 0