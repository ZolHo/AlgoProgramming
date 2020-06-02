class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if (len(s) < k) :
            return False

        chart = [0 for i in range(36)]
        theA = ord('a')
        for c in s:
            chart[ord(c)-theA] += 1
        orr, mul = 0, 0
        for i in chart:
            if (i%2==0 and i!=0):
                mul += i/2
            elif (i%2==1):
                orr += 1
                mul += i//2

        # for i in chart:
        #     print(i,end=" ")
        # print(orr,mul)
        if (orr > k) :
            return False
        elif (k-orr>2*mul):
            return False
        else:
            return True

#执行用时 :156 ms, 在所有 Python3 提交中击败了28.92%的用户
#内存消耗 :14.6 MB, 在所有 Python3 提交中击败了100.00%的用户

solu = Solution()
s = "aaa"
print(solu.canConstruct(s,3))

