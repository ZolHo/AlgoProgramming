class Solution:
    def minSpeedOnTime(self, dist, hour) :
        if hour < len(dist)-1 :
            return -1
        lo, hi = 1, max(dist)
        if int(hour)== len(dist) -1 :
            hi = int(max(hi, dist[-1]/(hour-int(hour)))) if hour >int(hour) else hi
        flag = True
        while flag:
            t = len(dist) - 1
            if t + dist[-1]/hi > hour:
                hi *= 2
            else : flag = False


        mid = (lo+hi)//2
        while lo < hi :
            t = 0
            for i in dist[:-1] :
                if i < mid :t += 1
                else :
                    k = i/mid
                    if k > int(k) : k = int(k) + 1
                    t += k
            t += dist[-1] / mid
            flag = t <= hour
            if flag :
                hi = mid
            else :
                lo = mid + 1
            mid = (lo + hi) //2
        return int(lo)