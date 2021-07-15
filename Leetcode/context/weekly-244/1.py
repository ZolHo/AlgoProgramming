class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        flag = True
        i2 = 0
        for i in range(n):
            j2 = 0
            for j in range(n):
                if mat[i][j] != target[i2][j2]: flag = False
                j2 += 1
            i2 += 1
        if flag: return True
        flag = True
        i2 = 0
        for j in range(n):
            j2 = 0
            for i in range(n)[::-1]:
                if mat[i][j] != target[i2][j2]: flag = False
                j2 += 1
            i2 += 1
        if flag: return True
        flag = True
        i2 = 0
        for i in range(n)[::-1]:
            j2 = 0
            for j in range(n)[::-1]:
                if mat[i][j] != target[i2][j2]: flag = False
                j2 += 1
            i2 += 1
        if flag: return True
        flag = True
        i2 = 0
        for j in range(n)[::-1]:
            j2 = 0
            for i in range(n):
                if mat[i][j] != target[i2][j2]: flag = False
                j2 += 1
            i2 += 1
        if flag: return True
        return False
