#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
class Solution {
public:
    int maxArea(vector<int>& height) {
        int left=0, right=height.size()-1;
        int ans = 0;
        while(left<right) {
            ans = max({min({height[left],height[right]})*(right-left), ans});
            if (height[left] < height[right]) {
                left++;
            } else right--;
        }
        return ans;

    }
};