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
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> ans;
        if(root==NULL)
            return ans;
        stack<TreeNode*> s;
        s.push(root);
        while(!s.empty())
        {
            TreeNode *t=s.top();
            if(t->left)
            {
                s.push(t->left);
                t->left=NULL;
            }
            else
            {
                //s.pop();
                if(t->right)
                {
                    s.push(t->right);
                    t->right=NULL;
                }
                else
                {
                    ans.push_back(t->val);
                    s.pop();
                }
            }
        }
        return ans;
        
    }
};
