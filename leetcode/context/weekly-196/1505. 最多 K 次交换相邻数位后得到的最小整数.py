# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 10:43 上午
# @Author  : ZolHo.github.io
# @FileName: 1505. 最多 K 次交换相邻数位后得到的最小整数.py

from typing import List

class Solution:
    def minInteger(self, num: str, k: int) -> str:
        p = num
        num = []
        for v in p:
            num.append(int(v))
        weishu = 0
        fuzhu = [[] for i in range(10)]
        for i, v in enumerate(num):
            fuzhu[v].append(i)

        jia = [0 for i in num]
        weizhi = [0 for i in num]

        for qq, vv in enumerate(jia):
            weizhi[qq + vv] = qq

        while weishu<len(num)-1 and k > 0:
            for i in range(num[weishu]):
                while True:
                    if fuzhu[i] and (fuzhu[i][0]+jia[fuzhu[i][0]] < weishu) :
                        fuzhu[i].pop(0)
                    else:break

                if not fuzhu[i]: continue
                j = fuzhu[i][0]+jia[fuzhu[i][0]]
                if j-weishu > k :continue
                else :
                    k = k-(j-weishu)
                    # tmp = weizhi[j]
                    for sb in range(weishu,j)[::-1]:
                        # print(weizhi[sb])
                        jia[weizhi[sb]] += 1
                        # weizhi[sb+1] = weizhi[sb]
                    # jia[fuzhu[i][0]] -= (j-weishu)
                    # weizhi[weishu] = tmp
                    print(weizhi)
                    weizhi.pop(j)
                    weizhi.insert(0,0)
                    fuzhu[i].pop(0)
                    num.pop(j)
                    num.insert(weishu,i)
                    break

            weishu+=1

        ans = ""
        for v in num:
            ans+=str(v)
        return ans

solu = Solution()
print(solu.minInteger("99998888777766665555666",2000))