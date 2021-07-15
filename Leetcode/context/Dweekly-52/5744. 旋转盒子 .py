from typing import List
from functools import reduce
import operator

class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        zhuanzhi = [[box[j][i] for j in range(len(box))[::-1]] for i in range(len(box[0]))]
        for i in range (len(zhuanzhi))[::-1] :
            for j in range(len(zhuanzhi[0])) :
                if zhuanzhi[i][j] == "#":
                    t = i
                    for k in range(i+1,len(zhuanzhi)) :

                        if zhuanzhi[k][j] == "." :
                            zhuanzhi[t][j], zhuanzhi[k][j] = ".", "#"
                            t = k
                        else:
                            break
        return zhuanzhi
