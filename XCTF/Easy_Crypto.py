# -*- coding: utf-8 -*-
# @Time    : 2020/11/5 10:59 上午
# @Author  : ZolHo.github.io
# @FileName: Easy_Crypto


s = [i  for i in range(256)]
t = [" " for i in range(256)]
key = "hello world"
for i in range(256):
    t[i] = key[(i) % (len(key))]

j = 0
for i in range (256):
    j = (j+s[i]+ord(t[i]))%256
    s[i], s[j] = s[j], s[i]

f = open("Easycrypto",mode="rb")
flag = f.read()

i , j= 0,0
ans = []
for m in range(37):
    # for p in range(200):
    i = (i+1)%256
    j = (j+s[i])%256
    s[i],s[j] = s[j], s[i]
    x = (s[i]+(s[j]%256))%256
    # print(flag[m], s[x])
    ans.append( chr(flag[m]^s[x]))

print("".join(ans))
