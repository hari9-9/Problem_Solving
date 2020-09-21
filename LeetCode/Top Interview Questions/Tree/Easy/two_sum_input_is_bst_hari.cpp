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
    void inorder(TreeNode* root ,vector<int>&elements)
    {
        if(!root)
            return;
        inorder(root->left,elements);
        elements.push_back(root->val);
        inorder(root->right,elements);
    }
    bool findTarget(TreeNode* root, int k) {
        vector<int>elements;
        inorder(root,elements);
        int n=elements.size();
        // for(int i=0;i<n;i++)
        // {
        //     cout<<elements[i]<<" ";
        // }
        int l=0;
        int r=n-1;
        while(l<r)
        {
            if(elements[l]+elements[r]==k)
                return true;
            else if(elements[l]+elements[r]>k)
                r--;
            else
                l++;
        }
        return false;;
        
    }
};
