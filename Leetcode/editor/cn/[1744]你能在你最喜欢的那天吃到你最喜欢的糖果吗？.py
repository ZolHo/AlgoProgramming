# 你能在你最喜欢的那天吃到你最喜欢的糖果吗？ 1744
# 2021-06-01 11:02:07

# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def canEat(self, candiesCount, queries):
        qsum = [i for i in candiesCount]
        ans = []
        for i in range(1,len(candiesCount)) :
            qsum[i] += qsum[i-1]
        for que in queries:
            a1, a2 = que[1]+1, (que[1]+1)*que[2]
            t1,t2 = len(candiesCount), len(candiesCount)
            for i in range(len(qsum)) :
                if a1<=qsum[i] :
                    t1 = i
                    break
            for i in range(len(qsum)) :
                if a2<=qsum[i] :
                    t2 = i
                    break
            ans.append(que[0]<=t2 and que[0]>=t1)
        return ans
# leetcode submit region end(Prohibit modification and deletion)
