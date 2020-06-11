# -*- coding: utf-8 -*-
# @Time    : 2020/6/11 5:31 下午
# @Author  : ZolHo
# @FileName: 739-daily-temperatures.py


class Solution:
    def dailyTemperatures(self, T):
        px = [(x,y) for x,y in  enumerate(T) ]
        px.sort(key =lambda ele:(ele[1],-ele[0]), reverse=True)
        ans = [0 for x in range(len(T))]
        ftmap = [False for x in range(len(T))]
        last_tem, last_no, ans[px[0][0]], ftmap[px[0][0]] = px[0][1], px[0][0], 0, True
        for ele in px[1:]:
            if (last_tem == ele[1] and ans[last_no]==0):
                ans[ele[0]] = 0
            elif (last_tem == ele[1] and last_no + ans[last_no] - ele[0] > 0):
                ans[ele[0]] = last_no + ans[last_no] - ele[0]
            else:
                for i in range(ele[0],len(T)):
                    if (ftmap[i]) :
                        ans[ele[0]] = i - ele[0]
                        break

            ftmap[ele[0]] = True
            last_no, last_tem = ele[0], ele[1]
        return ans


solu = Solution()
print (solu.dailyTemperatures([34,80,80,34,34,80,80,80,80,34]))
