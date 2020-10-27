# -*- coding: utf-8 -*-
# @Time    : 2020/10/27 17:36
# @Author  : ZolHo
# @FileName: 流浪者.py

abcd = "abcdefghiABCDEFGHIJKLMNjklmn0123456789opqrstuvwxyzOPQRSTUVWXYZ"
target = "KanXueCTF2019JustForhappy"
ans = [ abcd.find(target[i]) for i in range ( len (target))]
print(ans)
new = []
for i, value in enumerate(ans) :
    for j in range (0,200) :
        temp = j
        if j>57 or j <48 :
            if j>122 or j <97:
                if j>90 or j < 65:
                    continue
                else:
                    temp = j - 29
            else:
                temp = j-87
        else:
            temp = j - 48
        if temp == value:
            new.append(j)
            break
pp = ""
for i in new:
    pp += chr(i)
print(pp)