//求二叉树的层序遍历
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};
class Solution {
   public:
    /**
     * 
     * @param root TreeNode类 
     * @return int整型vector<vector<>>
     */
    vector<vector<int>> levelOrder(TreeNode *root) {
        if(!root) return vector<vector<int>>();
        queue<pair<TreeNode *, int>> q = {};
        q.push(make_pair(root, 1));
        vector<vector<int>> ans = {};
        vector<int> *tv;
        while (q.size()) {
            TreeNode *temp = q.front().first;
            int deep = q.front().second;
            q.pop();
            if (deep > ans.size()) {
                ans.push_back(vector<int>());
                tv = &ans[ans.size()-1];
            }
            tv->push_back(temp->val);
   
            if (temp->left) q.push(make_pair(temp->left, deep + 1));
            if (temp->right) q.push(make_pair(temp->right, deep + 1));
        }
        return ans;
    }
};