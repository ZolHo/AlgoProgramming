#include <iostream>
#include <math.h>
#include <stdio.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <stack>
#include <queue>

using namespace std;
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l = 0, r = nums.size()-1;
        while (l<r) {
            if (nums[l] < nums[r]) return nums[l];
            int mid = (l+r)/2;
            if (nums[mid] < nums[l]) r = mid;
            else l = mid+1;
        }
        return 0;
    }
};
int main() {
    Solution so;
    vector<int> a ({1,2,3});
    int ans = so.findMin(a);
    cout<<ans<<endl;
    return 0;
}
