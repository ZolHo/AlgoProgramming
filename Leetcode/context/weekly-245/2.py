from typing import List
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        isre = [False for _ in range(len(s))]
        for i in removable :
            isre[i] = True
        c = {}
        for i,v in enumerate(s):
            if not isre[i]:
                if v in c :c[v].append(i)
                else :c[v] = [i]
        di = -1
        flag = True
        for k in p :
            if k not in c :
                flag = False
                break
            temp = False
            c[k].sort()
            for j in c[k] :
                if j > di:
                    di = j
                    temp = True
                    break
            if not temp: flag = False
        if flag : return len(removable)
        for i, v in enumerate(removable[::-1]) :
            # print(c)
            if s[v] in c:c[s[v]].append(v)
            else:c[s[v]] = [v]
            di = -1
            flag = True
            for k in p:
                if k not in c:
                    flag = False
                    break
                temp = False
                c[k].sort()
                # print(k, c[k],di)
                for j in c[k]:
                    if j > di:
                        di = j
                        temp = True
                        break
                # print(di, temp)
                if not temp: flag = False
            if flag: return len(removable)-i-1
        return 0


