object Solution {
    def twoSum(nums: Array[Int], target: Int): Array[Int] = {
        
        @tailrec
        def solve(index: Int, seen: Map[Int, Int]): Array[Int] = {
            val complement = target - nums(index)

            if (seen.contains(complement)) {
                Array(seen(complement), index)
            } else {
                solve(index + 1, seen + (nums(index) -> index))
            }
        }

        solve(0, Map.empty)
        
    }
}