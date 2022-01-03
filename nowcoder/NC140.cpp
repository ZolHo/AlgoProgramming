//排序
#include <iostream>
#include <vector>
using namespace std;

class Solution {
   public:
    /**
     * 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
     * 将给定数组排序
     * @param arr int整型vector 待排序的数组
     * @return int整型vector
     */
    vector<int> MySort(vector<int> &arr) {
        if (!arr.size()) return arr;
        quickSort(arr, 0, arr.size() - 1);
        return arr;
    }
    void swap(int &a, int &b) {
        int temp = a;
        a = b;
        b = temp;
    }
    void quickSort(vector<int> &arr, int lf, int rt) {
        if (lf >= rt + 1) return;
        int l = lf, r = rt;
        while (l < r) {
            while (arr[l] < arr[r]) {
                r--;
            }
            if (l < r) {
                swap(arr[l], arr[r]);
                l++;
            }
            while (arr[r] > arr[l]) {
                l++;
            }
            if (l < r) {
                swap(arr[l], arr[r]);
                r--;
            }
        }
        quickSort(arr, lf, l - 1);
        quickSort(arr, l + 1, rt);
    }
};

int main() {
}