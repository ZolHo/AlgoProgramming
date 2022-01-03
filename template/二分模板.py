# @time   :2021/10/09
# @author :ZolHo
# @file   :二分模板.py

from typing import List

def 二分模板 ():

    选择右边 = True
    arr = [0 for i in range(10)]

    l = len(arr)
    lf, rt, mid = 0, l, l//2 #注意左闭右开，所以rt是大于区间的
    while lf<rt :
        if 选择右边 :
            lf = mid + 1
        else :
            rt = mid
        mid = (lf+rt)//2
    return mid