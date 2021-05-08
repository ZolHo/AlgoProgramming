from typing import List

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1=="0" or num2=='0' :
            return '0'
        ans = [['0' for j in range(len(num1)+len(num2))] for i in range(len(num1))]
        jinwei = 0
        for x,i in enumerate(num1[::-1]):
            for y,j in enumerate(num2[::-1]):
                temp = int(i) *int(j)+jinwei
                # print(i,j,temp,x,y)
                jinwei = temp//10
                ans[x][-y-x-1] = str(temp%10)
            if jinwei!=0:
                ans[x][-y-x-2] = str(jinwei)
                jinwei = 0
        for i in range(1,len(ans[0])+1) :
            sum = 0
            for j in range(len(ans)) :
                sum+=int(ans[j][-i])
            sum += jinwei
            jinwei = sum//10
            ans[0][-i] = str(sum%10)
        return "".join(ans[0]).lstrip("0")
so = Solution()
print(so.multiply("9","98"))



