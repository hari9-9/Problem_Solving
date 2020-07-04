/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(!root)
        {
            return {};
        }
        queue<TreeNode*> q;
        vector<vector<int>> result;
        vector<int> curr_vec;
        q.push(root);
        q.push(NULL);
        while(!q.empty())
        {
            TreeNode* curr =q.front();
            q.pop();
            if (curr==NULL)
            {
                result.push_back(curr_vec);
                curr_vec.resize(0);
                if(q.size()>0)
                {
                    q.push(NULL);
                }
            }
            else
            {
                curr_vec.push_back(curr->val);
                if(curr->left!=NULL)
                {
                    q.push(curr->left);
                }
                if(curr->right!= NULL)
                {
                    q.push(curr->right);
                }
            }
        }
        return result;
    }
};
