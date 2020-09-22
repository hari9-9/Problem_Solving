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
    void leaf_sequencer(TreeNode* root , vector<int>& leaf)
    {
        if(root==NULL)
            return;
        if(root->left==NULL && root->right==NULL)
        {
            leaf.push_back(root->val);
        }
        leaf_sequencer(root->left , leaf);
        leaf_sequencer(root->right , leaf);
        
    }
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int>l1,l2;
        leaf_sequencer(root1,l1);
        leaf_sequencer(root2,l2);
        return l1==l2;
        
    }
};
