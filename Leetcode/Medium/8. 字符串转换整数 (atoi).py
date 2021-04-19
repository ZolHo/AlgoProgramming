class Solution:
    def myAtoi(self, s: str) -> int:
        fanwei = [-2**31, 2**31 -1]
        if len(s)==0 :
            return 0
        numbers = "0123456789"
        s1=s.strip(" ")
        s=s1.lstrip('0')
        if len(s) == 0:
            return 0
        ans = 0
        sigh = 1
        if s[0] in "+-":
            if s1[0] =='0' :
                return 0
            sigh-=2*"+-".find(s[0])
            s = s[1:]
        flag = False
        for i in s:
            t = numbers.find(i)

            if -1 == t:
                break
            ans = 10*ans +t
        ans *= sigh
        if ans< fanwei[0] :
            return fanwei[0]
        else:
            return ans if ans< fanwei[1] else fanwei[1]


