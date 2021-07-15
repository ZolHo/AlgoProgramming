class Solution:
    def minFlips(self, s: str) -> int:
        temp = s
        n = len(s)
        anser = n
        t = 2
        for i in range(n) :
            if temp[i:i+t] == "0"*t or temp[i:i+t] == "1"*t:
                s = temp[i+t//2:] + temp[:i+t//2]
                t+=1
            else:continue
            t1,t2 = [], []
            for i in range(n) :
                if i %2 ==0 :
                    t1.append("0")
                    t2.append("1")
                else :
                    t1.append("1")
                    t2.append("0")
            s1, s2 = "".join(t1), "".join(t2)
            an1, an2 = 0, 0
            for i in range(n) :
                if s1[i] != s[i] : an1 += 1
                if s2[i] != s[i] : an2 += 1
            anser =  min(anser,an1, an2)
        return anser
