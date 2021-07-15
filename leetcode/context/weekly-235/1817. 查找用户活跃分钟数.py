from typing import List

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        logdict = {}
        for i in logs:
            if i[0] in logdict:
                logdict[i[0]].add(i[1])
            else :
                logdict[i[0]] = set([i[1]])
                
        ans = [0 for i in range(k)]
        for key in logdict:
            ans[len(logdict[key])-1] += 1
        return ans

so = Solution() 
print(so.findingUsersActiveMinutes([[1,1]], 2))

