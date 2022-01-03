//寻找第K大
#include <iostream>
#include <vector>
using namespace std;

class Solution {
   public:
    int findKth(vector<int> a, int n, int K) {
        return quickSeachK(a, K, 0, n - 1);
    }

    int quickSeachK(vector<int> &a, const int &k, int lf, int rt) {
        //if (lf >= rt) return a[lf];
        int l = lf, r = rt;
        while (l < r) {
            while (a[l] > a[r]) --r;
            if (l < r) {
                swap(a[l], a[r]);
                ++l;
            }
            while (a[l] > a[r]) ++l;
            if (l < r) {
                swap(a[l], a[r]);
                --r;
            }
        }
        if (l > k)
            return quickSeachK(a, k, lf, l - 1);
        else if (l < k)
            return quickSeachK(a, k, l + 1, rt);
        else
            return a[l];
    }
};