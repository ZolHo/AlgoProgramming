from typing import List
from collections import deque
import queue
import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        lenth = len(tasks)
        for i in range(lenth) :
            tasks[i].append(i)
        tasks.sort(key = lambda x: x[0])
        ans = [0 for i in range (lenth)]
        youxian = queue.PriorityQueue()
        now = tasks[0][0]
        for i in range (lenth):
            if (now < tasks[i][0]) :
                now = tasks[i][0]
            for j in range(i+youxian.qsize(), lenth):
                if tasks[j][0] <= now:
                    youxian.put([tasks[j][1], tasks[j][2]])
                else:
                    break
            renwu = youxian.get()
            now+=renwu[0]
            ans[i] = renwu[1]
        return ans


so = Solution()
print(so.getOrder([[19,13],[16,9],[21,10],[32,25],[37,4],[49,24],[2,15],[38,41],[37,34],[33,6],[45,4],[18,18],[46,39],[12,24]]))