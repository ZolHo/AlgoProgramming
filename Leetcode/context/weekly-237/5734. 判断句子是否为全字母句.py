from typing import List

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        ans = [False for i in range(26)]
        for i in sentence:
            ans[ord(i)-ord('a')] = True

        print(ans)
        for i in ans:
            if i==False:

                return False
        return True



so = Solution()
print(so.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))