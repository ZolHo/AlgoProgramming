from typing import List
from functools import reduce
import operator

class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        i = 0
        while True:
            i+=1
            if memory1 >= memory2 :
                memory1 -= i
                if memory1<0 :
                    memory1 += i
                    break
            else:
                memory2 -= i
                if memory2 < 0 :
                    memory2 += i
                    break
        return [i, memory1, memory2]

