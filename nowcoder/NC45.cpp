//实现二叉树先序，中序和后续遍历
#include <iostream>
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
     * @param root TreeNode类 the root of binary tree
     * @return int整型vector<vector<>>
     */
    vector<vector<int> > threeOrders(TreeNode *root) {
        // write code here
        vector<vector<int>> ans = {};
        frontSearch(root);
        midtSearch(root);
        backSearch(root);
        ans.push_back(this->m_front);
        ans.push_back(this->m_mid);
        ans.push_back(this->m_back);
        return ans;
    }

    void frontSearch(TreeNode *node) {
        if (!node) return;
        this->m_front.push_back(node->val);
        frontSearch(node->left);
        frontSearch(node->right);
    }
    
    void midtSearch(TreeNode *node) {
        if (!node) return;
        midtSearch(node->left);
        this->m_mid.push_back(node->val);
        midtSearch(node->right);
    }
    
    void backSearch(TreeNode *node) {
        if(!node) return;
        backSearch(node->left);
        backSearch(node->right);
        this->m_back.push_back(node->val);
    }

    private:
    vector<int> m_front={};
    vector<int> m_mid={};
    vector<int> m_back={};
    
};