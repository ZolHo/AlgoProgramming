#include<iostream>
#include<unordered_set>
#include<unordered_map>
#include<algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        if (nums.size() < 3) return ans;
        unordered_map<int, int> exist_map;
        unordered_set<int> used_set;
        for (auto p: nums) {
            if(exist_map.find(p)!=exist_map.end()) exist_map[p] ++;
            else exist_map[p] = 1;
        }
        sort(nums.begin(),nums.end());
        for (int i = 0; i < nums.size()-1; ++i ) {
            if (nums[i] >= 0 || used_set.find(nums[i])!=used_set.end()) continue;
            used_set.insert(nums[i]);
            exist_map[nums[i]] --;
            for (int j = i+1; j < nums.size(); ++j) {
                if(nums[i]+nums[j] > 0 || (j>i+1 && nums[j]==nums[j-1]) || -(nums[i]+nums[j])<nums[j]) continue;
                exist_map[nums[j]]--;
                if (exist_map.find(-(nums[i]+nums[j]))!=exist_map.end() && exist_map[-(nums[i]+nums[j])]>0)
                {
                    ans.push_back(vector<int> ({nums[i],nums[j],-(nums[i]+nums[j])}));
                }
                exist_map[nums[j]]++;
            }
            exist_map[nums[i]]++;
        }
        if (exist_map.find(0)!=exist_map.end() && exist_map[0]>=3) ans.push_back({0,0,0});
        
        return ans;
    }
};