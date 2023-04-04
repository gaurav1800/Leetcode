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
        
        if(root == null) {
            return new ArrayList<>();
        }
        
        List<List<Integer>> result = new ArrayList<>();
        
        Queue<TreeNode> q = new ArrayDeque<>(Arrays.asList(root));
        
        while(!q.isEmpty()) {
            List<Integer> currentlvl = new ArrayList<>();
            for(int i = q.size(); 0 < i; --i) {
                TreeNode node = q.poll();
                currentlvl.add(node.val);
                if (node.left != null) {
                    q.offer(node.left);
                }
                if (node.right != null) {
                    q.offer(node.right);
                }
            }
            result.add(currentlvl);
        }
        
        return result;
    }
}