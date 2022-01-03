#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    /**
     * 
     * @param numbers int整型vector 
     * @param target int整型 
     * @return int整型vector
     */
    vector<int> twoSum(vector<int>& numbers, int target) {
        unordered_map<int, int> num_set = {};
        vector<int> ans = {};
        for (int i = 0; i < numbers.size(); ++i) {
            if (num_set.find(numbers[i]) != num_set.end()) 
            {
                if (numbers[i]*2==target) {
                    ans.push_back(num_set[numbers[i]]+1);
                    ans.push_back(i+1);
                    return ans;
                }
            }
            
            num_set.insert(make_pair(numbers[i], i));
        }
        for (int i = 0 ; i < numbers.size(); i ++) {
            if (numbers[i]!=(target-numbers[i]) && num_set.find(target-numbers[i])!=num_set.end()) {
                ans.push_back(i+1);
                ans.push_back(num_set[target-numbers[i]]+1);
                return ans;
            }
        }
        return ans;
    }
};