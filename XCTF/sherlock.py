# -*- coding: utf-8 -*-
# @Time    : 2020/11/3 9:33 上午
# @Author  : ZolHo.github.io
# @FileName: sherlock

daxie = "QWERTYUIOPASDFGHJKLZXCVBNM{}_"
ans = []
with open('sherlock.txt', 'r') as f:
    for line in f.readlines():
        for i in line:
            if i in daxie:
                ans.append(i)
                # print(i)
h = "".join(ans)
i = 0
fina = []
while i<len(h):
    if h[i] == 'O':
        i+=3
        fina.append('1')
    else:
        i+=4
        fina.append('0')
m = "".join(fina)
print(m)


