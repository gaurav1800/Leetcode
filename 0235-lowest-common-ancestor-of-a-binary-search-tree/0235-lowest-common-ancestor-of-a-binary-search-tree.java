/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        
        if (root == null) {
            return root;
        }
        
        TreeNode ptr = root;
        while(true) {
            if (ptr == p || ptr == q) {
                return ptr;
            }
            else if ((p.val < ptr.val && ptr.val < q.val) || (p.val > ptr.val && ptr.val > q.val)) {
                return ptr;
            }
            else if (ptr.val > p.val && ptr.val > q.val) {
                ptr = ptr.left;
            }
            else {
                ptr = ptr.right;
            }
        }
        
    }
}