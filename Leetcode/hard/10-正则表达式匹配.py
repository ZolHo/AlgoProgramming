# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 9:56 上午
# @Author  : ZolHo.github.io
# @FileName: 10-正则表达式匹配.py

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        print(s,p)
        if(len(p)==0 and len(s)==0) : return True
        if (len(p)==0 and len(s)!=0) : return False
        if (len(s)==0) : return True if (p.count('*')== len(p)/2) else False
        i_s, i_p = 0, 0
        while(i_p<len(p) and i_s<len(s)):
            if (i_p<len(p)-1 and p[i_p:i_p+2]=='.*' ) :
                for j in range(i_s, len(s)+1) :
                    if (self.isMatch(s[j:], p[i_p+2:])) : return True
                return False
            elif (p[i_p]=='.') :
                i_s += 1
            elif (i_p<len(p)-1 and p[i_p+1]=='*') :
                last, j = p[i_p], i_s
                if (self.isMatch(s[j:], p[i_p + 2:])): return True
                while (j<len(s)):
                    if (last!=s[j]) : break
                    elif(self.isMatch(s[j+1:], p[i_p + 2:])) :return True
                    j+=1
                return False
            else :
                if (s[i_s]!=p[i_p]) : return False
                else: i_s+=1
            i_p+=1
        return self.isMatch(s[i_s:],p[i_p:])



solu = Solution()
print(solu.isMatch(""
,"c*ab"))