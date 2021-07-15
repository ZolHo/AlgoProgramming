from typing import List
class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        jobs.sort()
        jobs = jobs[::-1]
        lo, hi = max(jobs), sum(jobs[::k])+1
        mid = (lo+hi)//2

        def test_ok(top) :
            is_vis = [False for i in jobs]
            for j in range(k) :
                remind = top
                for i in range (len(jobs)):
                    if is_vis[i] ==False and remind > jobs[i] :
                        remind -= jobs[i]
                        is_vis[i] = True
            return sum(is_vis) == len(jobs)
        while True :
            print(lo,hi,mid)
            if test_ok(mid) :
                hi = mid
            else:
                lo = mid+1

            mid = (lo+hi)//2
            if lo >= hi : return lo
