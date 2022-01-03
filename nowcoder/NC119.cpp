//最小的K个数
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

// static int cont = 0;
class Solution {
   public:
    vector<int> GetLeastNumbers_Solution(vector<int> input, int k) {
        vector<int> &m_minHeap = input;
        vector<int> ans = {};
        if (!input.size()) return ans;
        buildHeap(m_minHeap);
        for (int i = 0; i < k; i++) {
            ans.push_back(popMin(m_minHeap));
        }
//         cout<<input.size()<<" "<<cont<<endl;
        return ans;
    }

    void buildHeap(vector<int> &h) {
        unsigned int len = h.size();
        for (int i = floor((len - 2) / 2); i >= 0; --i) {
            if (i * 2 + 1 < len) {
                if (h[i] > h[i * 2 + 1]) {
                    swap(h[i], h[i * 2 + 1]);
                    downShift(h, i * 2 + 1);
                }
            }
            if (i * 2 + 2 < len) {
                if (h[i] > h[i * 2 + 2]) {
                    swap(h[i], h[i * 2 + 2]);
                    downShift(h, i * 2 + 2);
                }
            }
        }
    }

    void downShift(vector<int> &h, int pos) {
//         cont ++ ;
        if (pos * 2 + 1 >= h.size()) return;
        if (pos * 2 + 2 < h.size()) {
            int t = h[pos * 2 + 1] < h[pos * 2 + 2] ? pos * 2 + 1 : pos * 2 + 2;
            if (h[pos] > h[t]) {
                swap(h[pos], h[t]);
                downShift(h, t);
            }
        } else {
            if (h[pos] > h[pos * 2 + 1]) {
                swap(h[pos], h[pos * 2 + 1]);
                downShift(h, pos * 2 + 1);
            }
        }
    }

    int popMin(vector<int> &h) {
        int rs = h[0];
        h[0] = h[h.size() - 1];
        h.resize(h.size() - 1);
        downShift(h, 0);
       
        return rs;
    }

   
};