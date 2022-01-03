#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        unordered_map<int, int> m_num;
        vector<int> ans;
        int le = numbers.size();
        for (int i = 0; i < le; ++i) {
            int t = target - numbers[i];
            if (t>numbers[le-1] ) continue;
            if (m_num.find(t) != m_num.end()) {
                if (m_num[t] != -1) {
                    ans = {i, m_num[t]};
                    return ans;
                } else {
                    continue;
                }
            } else {
                m_num[t] = bit_find(numbers, i, le, t);
                if (m_num[t]!= -1) {
                    ans = {i, m_num[t]};
                    return ans;
                }
            }
        }
        return ans;

    }

    int bit_find(vector<int> & numbers, int lf, int rt, int target) {
        int l = lf, r = rt, mid = (lf+rt)/2;
        while(l<r) {
            if (target==numbers[mid]) return mid;
            if (numbers[mid]<target) l = mid+1;
            else r = mid;
            mid = (l+r)/2;
        }
        return target==numbers[mid]?mid:-1;
    }
};