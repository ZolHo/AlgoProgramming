# -*- coding: utf-8 -*-
# @Time    : 2020/6/8 9:26 上午
# @Author  : ZolHo
# @FileName: 990-satisfiability-of-equality-equations.py

class Solution:#并查集
    def find_x(self, dict_arr,x):
        return x if x==dict_arr[x] else self.find_x(dict_arr,dict_arr[x])

    def equationsPossible(self, equations) -> bool:
        dict_arr = {}
        for str in equations:
            dict_arr[str[0]], dict_arr[str[3]] = str[0], str[3]
        for str in equations:
            if (str[1]=='='):
                dict_arr[self.find_x(dict_arr, str[0])] = dict_arr[self.find_x(dict_arr, str[3])]
        for str in equations:
            if (str[1]=='!'):
                if (self.find_x(dict_arr, str[0])==self.find_x(dict_arr, str[3])):
                    return False

        return True

#执行用时 :56 ms, 在所有 Python3 提交中击败了77.67%的用户
#内存消耗 :13.8 MB, 在所有 Python3 提交中击败了33.33%的用户

solu = Solution()
print(solu.equationsPossible(["a==b","e==c","b==c","a!=e"]))

