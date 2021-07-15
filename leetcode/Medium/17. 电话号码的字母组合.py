class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        temp =["abc", "def", "ghi","jkl","mno","pqrs","tuv","wxyz"]
        if digits=="":
            return []
        ans=[[] for i in range(len(digits)+1)]
        ans[0].append("")
        for i in range (len(digits)):
            for j in range(len(ans[i])):
                for k in temp[ord(digits[i])-ord('2')]:
                    ans[i+1].append(ans[i][j]+k)
        return ans[-1]