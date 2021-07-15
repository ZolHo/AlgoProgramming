class Solution:
    #剪枝
    def subarrayBitwiseORs(self, A) -> int:
        A = [1, 2, 3]
        s, h = set(A), A[0]
        
        for i in A:
            h = h | i
        s.add(h)

        for i in range(len(A)):
            tmp = A[i]
            for j in range(i, len(A)):
                tmp = tmp | A[j]
                if (tmp == h):
                    break
                # print(tmp,i,j)
                s.add(tmp)
        return len(s);


A = [1, 2, 3]
solu = Solution()
print(solu.subarrayBitwiseORs(A))
