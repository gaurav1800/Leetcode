/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        
        List<List<Integer>> list = new ArrayList<List<Integer>>();
        Queue<TreeNode> q = new LinkedList<>();
        
        if (root == null) {
            return list;
        }
        q.add(root);
        
        while(!q.isEmpty()) {
            int lvl = q.size();
            List<Integer> currentlvl = new ArrayList<>();
            for(int i=0; i<lvl; i++) {
                if (q.peek().left != null) {
                    q.add(q.peek().left);
                }
                if (q.peek().right != null) {
                    q.add(q.peek().right);
                }
                currentlvl.add(q.poll().val);
            }
            list.add(currentlvl);
        }
        
        return list;
        
    }
}