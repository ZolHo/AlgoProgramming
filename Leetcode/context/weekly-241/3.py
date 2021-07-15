from typing import List
from collections import Counter
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.n1, self.n2 = nums1, nums2
        self.c1, self.c2 = Counter(nums1), Counter(nums2)


    def add(self, index: int, val: int) -> None:
        t = self.n2[index]
        self.c2[t] -= 1
        if self.c2[t] == 0:
            self.c2.pop(t)
        if t+val in self.c2 : self.c2[t+val] +=1
        else: self.c2[t+val] = 1
        self.n2[index] += val

    def count(self, tot: int) -> int:

        anser = 0

        for i in self.c1.keys():
            if tot-i in self.c2:
                anser += self.c1[i] * self.c2[tot-i]

        return anser



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)