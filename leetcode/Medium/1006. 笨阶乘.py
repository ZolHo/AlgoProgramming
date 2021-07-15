class Solution:
    def clumsy(self, N: int) -> int:
        ans = 0
        a = N
        if a==3:
            return 6
        elif a==2:
            return 2
        elif a==1:
            return 1
        ans = a*(a-1)//(a-2) +(a-3)
        def digui(temp):
            nonlocal ans
            if temp==3:
                ans -= 6
                return
            elif temp == 2:
                ans -= 2
                return
            elif temp==1:
                ans -= 1
                return
            elif temp <= 0:
                return
            a = temp
            ans -= a*(a-1)//(a-2)
            ans += a-3
            digui(temp-4)
        digui(N-4)
        return ans