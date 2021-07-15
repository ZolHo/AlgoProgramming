# -*- coding: utf-8 -*-
# @Time    : 2020/10/8 10:54 上午
# @Author  : ZolHo.github.io
# @FileName: 12-整数转罗马数字


from typing import List
class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        if num//1000>0:
            for i in range(num//1000):
                ans += "M"
            num = num% 1000
        if num//900>0:
            ans += 'CM'
            num-=900
        if num//500>0:
            for i in range(num//500):
                ans +='D'
            num%=500
        if num//400>0:
            ans +='CD'
            num -= 400
        if num //100>0:
            for i in range(num//100):
                ans+='C'
            num%=100
        if num//90>0:
            ans+='XC'
            num-=90
        if num//50>0:
            for i in range(num//50):
                ans+='L'
            num%=50
        if num//40>0:
            ans+='XL'
            num-=40
        if num //10>0 :
            for i in range (num//10):
                ans+='X'
            num%=10
        if num//9>0:
            ans+='IX'
            num -=9
        if num//5>0:
            for i in range(num//5):
                ans+='V'
            num%=5
        if num//4>0:
            ans+='IV'
            num%=4
        for i in range(num):
            ans+="I"
        return ans
solu = Solution()
print(solu)