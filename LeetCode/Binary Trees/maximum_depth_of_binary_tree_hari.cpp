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
    int answer;
    void depth_top_down(TreeNode* root , int depth)
    {
        if (!root) {
        return;
    }
    if (!root->left && !root->right) {
        answer = max(answer, depth);
    }
    depth_top_down(root->left, depth + 1);
    depth_top_down(root->right, depth + 1);
    }
    int maxDepth(TreeNode* root) {
        depth_top_down(root,1);
        return answer;
    }
};
