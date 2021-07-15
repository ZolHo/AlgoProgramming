class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        t1, t2, last = 0, 0, s[0]
        t1m, t2m = 0, 0
        if last == '1': t1 = 1
        for i in s[1:]:
            if i == '1' and last == '1':
                t1 += 1
            elif i == '1':
                t1 = 1
            else:
                t1 = 0
            last = i
            t1m = max(t1, t1m)
        last = s[0]
        if last == '0': t2 = 1
        for i in s[1:]:
            if i == '0' and last == '0':
                t2 += 1
            elif i == '0':
                t2 = 1
            else:
                t2 = 0
            last = i
            t2m = max(t2, t2m)
        t1m = max(t1, t1m)
        t2m = max(t2, t2m)
        return t1m > t2m
