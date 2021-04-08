# -*- coding: utf-8 -*-
# @Time    : 2020/11/2 2:13 下午
# @Author  : ZolHo.github.io
# @FileName: XOR
from toolkit import HEX


sb = 0x0e0b213f26041e
xo = 0xff
k = 6
string = "crypto{"
while sb>0:
    temp = (sb&xo)
    sb = sb>>8
    for i in range(1000) :
        if temp ^ i == ord(string[k]) :
            print((chr(i)))
            break
    k-=1
