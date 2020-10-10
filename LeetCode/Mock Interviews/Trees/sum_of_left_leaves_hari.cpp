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
    void traverser(TreeNode* root , int& sum , bool l)
    {
        if( root && root->left==NULL && root->right==NULL)
        {
            if(l)
            {
                sum+=root->val;
                //cout<<sum<<" ";
            }
            return;
        }
        if(root)
        {
            traverser(root->left , sum , true);
            traverser(root->right , sum , false);
        }
        
    }
    int sumOfLeftLeaves(TreeNode* root) {
        int sum=0;
        traverser(root ,sum,false);
        return sum;
        
    }
};
