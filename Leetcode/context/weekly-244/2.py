from collections import Counter
class Solution:
    def reductionOperations(self, nums) -> int:
        c = Counter(nums)
        sotnums = list(c.keys())
        sotnums.sort()
        sotnums = sotnums[::-1]
        anser = 0
        t = c[sotnums[0]]
        for i in sotnums[1:]:
            anser+= t
            t += c[i]
        return anser
