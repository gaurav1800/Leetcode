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
        
        return isSymmetric(root, root);
        
        
    }
    
    bool isSymmetric(TreeNode *l, TreeNode *r) {
        if (!l || !r) {
            return l == r;
        }
        return l->val == r->val && isSymmetric(l->left, r->right) && isSymmetric(l->right, r->left);
    }
};