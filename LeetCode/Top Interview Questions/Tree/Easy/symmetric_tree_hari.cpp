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
    bool check_mirror(TreeNode* root1 , TreeNode* root2)
    {
        if(root1==NULL && root2==NULL)
        {
            return true;
        }
        if(root1 && root2 && root1->val == root2->val)
        {
            return (check_mirror( root1->left , root2->right ) && check_mirror(root1->right , root2->left ));
        }
        return false;
    }
    
    bool isSymmetric(TreeNode* root) {
        return check_mirror(root,root);
        
    }
};

// second attempt

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
    bool isSymmetric(TreeNode* root) {
        return mirror(root,root);
        
    }
    bool mirror(TreeNode* l , TreeNode* r)
    {
        if(l==NULL && r==NULL)
        {
            return true;
        }
        if(l && r && l->val == r->val)
        {
            return mirror(l->right,r->left) && mirror(l->left,r->right);
        }
        return false;
        
    }
};
