# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 11:21 下午
# @Author  : ZolHo.github.io
# @FileName: 树状数组.py

class bitTree():
    def __init__(self, arr) :
        self.n = len(arr)
        self.a = [0 for i in range(self.n+1)]
        for i in range(self.n):
            self.update(i, arr[i])

    def lowbit(self, i) :
        return i & -i;

    def update (self, i,  val) :
        i = i+1
        while i <= self.n :
            self.a[i] += val;
            i += self.lowbit(i);

    def sum (self, i) :
        i = i+1
        ret = 0;
        while i > 0 :
            ret += self.a[i];
            i -= self.lowbit(i);
        return ret;

class bitTreeQJXG():
    def __init__(self, arr, n) :
        self.n = n
        self.a = [0 for i in range(n+1)]
        self.update(0,arr[0])
        for i in range(1,n):
            self.update(i, arr[i]-arr[i-1])

    def lowbit(self, i) :
        return i & -i;

    def update (self, i,  val) :
        i = i+1
        while i <= self.n:
            self.a[i] += val
            i += self.lowbit(i)

    def range_update(self,l,r,val):
        self.update(l,val)
        self.update(r+1, -val)

    def get (self, i) :
        i = i+1
        ret = 0;
        while i > 0 :
            ret += self.a[i];
            i -= self.lowbit(i);
        return ret;

bt = bitTree([1,2,3,2,1,2,3],7)
# print(bt.sum(6))
bs = bitTreeQJXG([1,2,3,4,5,6,7,8],8)
bs.range_update(0,6,100)
print(bs.get(0),bs.get(7))