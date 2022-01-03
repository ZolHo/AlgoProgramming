#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

class Solution {
   public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 1) return strs[0];
        int ans = strs[0].size();
        for (int i = 1; i < strs.size(); ++i) {
            if (strs[i].size() > 0) {
                ans = min({ans, (int)strs[i].size()});
                for (int j = 0; j < ans; j++) {
                    if (strs[i][j] != strs[i - 1][j]) {
                        ans = j;
                        break;
                    }
                }
            } else
                return "";
        }
        return strs[0].substr(0, ans);
    }
};
