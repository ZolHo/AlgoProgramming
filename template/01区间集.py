# @time   :2021/07/13
# @author :ZolHo
# @file   :01区间集.py

class ZoIntervalArr():
    def __init__(self):
        self.arr = []

    # 返回交点，无交点返回0
    def add(self, left, right):
        arr = self.arr
        if len(arr) == 0 :
            arr.append((left, right))
            return []
        rs = None
        for i, temp in enumerate(arr) :
            if   left < temp[0] and right >= temp[0] :
                self.arr[i] = (left, max(temp[1], right))
                rs = [temp[0]] if right <= temp[0] else [temp[0], temp[1]]
            if left <= temp[1] and right > temp[1] :
                self.arr[i] = (min(left, temp[0]), right)
                rs = [temp[1]] if left >= temp[0] else [temp[0], temp[1]]
            elif temp[0] <= left and temp[1] >= right :
                return []
            elif temp[0] > right or (i == len(arr) - 1 and not rs):
                self.arr.append((left, right))
                rs = [left, right]
            if rs : break
        self.arr.sort()
        flag = True
        while flag:
            flag = False
            for i in range(len(self.arr) - 1):
                if self.arr[i][1] >= self.arr[i + 1][0]:
                    flag = True
                    if self.arr[i][1] >= self.arr[i + 1][1]: rs.append(arr[i + 1][1])
                    self.arr[i] = (self.arr[i][0], max(self.arr[i][1], self.arr[i + 1][1]))
                    self.arr.pop(i + 1)
                    break
        return rs

    def is_cover(self, k):
        for t in self.arr:
            if k <= t[1] and k >= t[0] : return True
            return False
